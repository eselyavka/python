#!/usr/bin/env python
import psycopg2
import logging
import getopt
import os
import sys
import pdb

host = 'localhost'
dbname = 'database'
user = 'user'
password = 'password'
port = 5432
critical = '80,80,52428800,1073741824'
warning = 'aa,50,524288000,5368709120'
verbose = None

def BloatTableSQL():
    return """
SELECT current_database()
 ,schemaname
 ,tblname
 ,bs * tblpages AS real_size
 ,(tblpages - est_num_pages) * bs AS bloat_size
 ,tblpages
 ,is_na
 ,CASE 
  WHEN tblpages - est_num_pages > 0
   THEN 100 * (tblpages - est_num_pages) / tblpages::FLOAT
  ELSE 0
  END AS bloat_ratio
FROM (
 SELECT ceil(reltuples / ((bs - page_hdr) / tpl_size)) + ceil(toasttuples / 4) AS est_num_pages
  ,tblpages
  ,bs
  ,tblid
  ,schemaname
  ,tblname
  ,heappages
  ,toastpages
  ,is_na
 FROM (
  SELECT (
    4 + tpl_hdr_size + tpl_data_size + (2 * ma) - CASE 
     WHEN tpl_hdr_size % ma = 0
      THEN ma
     ELSE tpl_hdr_size % ma
     END - CASE 
     WHEN ceil(tpl_data_size)::INT % ma = 0
      THEN ma
     ELSE ceil(tpl_data_size)::INT % ma
     END
    ) AS tpl_size
   ,bs - page_hdr AS size_per_block
   ,(heappages + toastpages) AS tblpages
   ,heappages
   ,toastpages
   ,reltuples
   ,toasttuples
   ,bs
   ,page_hdr
   ,tblid
   ,schemaname
   ,tblname
   ,is_na
  FROM (
   SELECT tbl.oid AS tblid
    ,ns.nspname AS schemaname
    ,tbl.relname AS tblname
    ,tbl.reltuples
    ,tbl.relpages AS heappages
    ,coalesce(toast.relpages, 0) AS toastpages
    ,coalesce(toast.reltuples, 0) AS toasttuples
    ,current_setting('block_size')::NUMERIC AS bs
    ,CASE 
     WHEN version() ~ 'mingw32'
      OR version() ~ '64-bit|x86_64|ppc64|ia64|amd64'
      THEN 8
     ELSE 4
     END AS ma
    ,24 AS page_hdr
    ,23 + CASE 
     WHEN MAX(coalesce(null_frac, 0)) > 0
      THEN (7 + count(*)) / 8
     ELSE 0::INT
     END + CASE 
     WHEN tbl.relhasoids
      THEN 4
     ELSE 0
     END AS tpl_hdr_size
    ,sum((1 - coalesce(s.null_frac, 0)) * coalesce(CASE 
       WHEN t.typlen = - 1
        THEN CASE 
          WHEN s.avg_width < 127
           THEN s.avg_width + 1
          ELSE s.avg_width + 4
          END
       WHEN t.typlen = - 2
        THEN s.avg_width + 1
       ELSE t.typlen
       END, 1024)) AS tpl_data_size
    ,bool_or(att.atttypid = 'pg_catalog.name'::regtype) AS is_na
   FROM pg_attribute AS att
   JOIN pg_type AS t ON att.atttypid = t.oid
   JOIN pg_class AS tbl ON att.attrelid = tbl.oid
   JOIN pg_namespace AS ns ON ns.oid = tbl.relnamespace
   JOIN pg_stats AS s ON s.schemaname = ns.nspname
    AND s.tablename = tbl.relname
    AND s.inherited = false
    AND s.attname = att.attname
   LEFT JOIN pg_class AS toast ON tbl.reltoastrelid = toast.oid
   WHERE att.attnum > 0
    AND NOT att.attisdropped
    AND tbl.relkind = 'r'
    AND ns.nspname NOT IN (
     'information_schema'
     ,'pg_catalog'
     )
   GROUP BY 1
    ,2
    ,3
    ,4
    ,5
    ,6
    ,7
    ,8
    ,9
    ,10
    ,tbl.relhasoids
   ORDER BY 2
    ,3
   ) AS s
  ) AS s2
 ) AS s3
"""

def BloatIndexSQL():
    return """
SELECT current_database()
 ,nspname AS schemaname
 ,tblname
 ,idxname
 ,bs * (sub.relpages)::BIGINT AS real_size
 ,bs * est_pages::BIGINT AS estimated_size
 ,bs * (sub.relpages - est_pages)::BIGINT AS bloat_size
 ,100 * (sub.relpages - est_pages)::FLOAT / sub.relpages AS bloat_ratio
 ,is_na
FROM (
 SELECT bs
  ,nspname
  ,table_oid
  ,tblname
  ,idxname
  ,relpages
  ,coalesce(1 + ceil(reltuples / floor((bs - pageopqdata - pagehdr) / (4 + nulldatahdrwidth)::FLOAT)), 0 -- ItemIdData size + computed avg size of a tuple (nulldatahdrwidth)
  ) AS est_pages
  ,is_na
  FROM (
  SELECT maxalign
   ,bs
   ,nspname
   ,tblname
   ,idxname
   ,reltuples
   ,relpages
   ,relam
   ,table_oid
   ,(
    index_tuple_hdr_bm + maxalign - CASE
     WHEN index_tuple_hdr_bm % maxalign = 0
      THEN maxalign
     ELSE index_tuple_hdr_bm % maxalign
     END + nulldatawidth + maxalign - CASE
     WHEN nulldatawidth = 0
      THEN 0
     WHEN nulldatawidth::INTEGER % maxalign = 0
      THEN maxalign
     ELSE nulldatawidth::INTEGER % maxalign
     END
    )::NUMERIC AS nulldatahdrwidth
   ,pagehdr
   ,pageopqdata
   ,is_na
  FROM (
   SELECT i.nspname
    ,i.tblname
    ,i.idxname
    ,i.reltuples
    ,i.relpages
    ,i.relam
    ,a.attrelid AS table_oid
    ,current_setting('block_size')::NUMERIC AS bs
    ,CASE -- MAXALIGN: 4 on 32bits, 8 on 64bits (and mingw32 ?)
     WHEN version() ~ 'mingw32'
      OR version() ~ '64-bit|x86_64|ppc64|ia64|amd64'
      THEN 8
     ELSE 4
     END AS maxalign
    ,
    24 AS pagehdr
    ,
    16 AS pageopqdata
    ,
    CASE 
     WHEN max(coalesce(s.null_frac, 0)) = 0
      THEN 2 -- IndexTupleData size
     ELSE 2 + ((32 + 8 - 1) / 8) -- IndexTupleData size + IndexAttributeBitMapData size ( max num filed per index + 8 - 1 /8)
     END AS index_tuple_hdr_bm
    ,
    sum((1 - coalesce(s.null_frac, 0)) * coalesce(s.avg_width, 1024)) AS nulldatawidth
    ,max(CASE 
      WHEN a.atttypid = 'pg_catalog.name'::regtype
       THEN 1
      ELSE 0
      END) > 0 AS is_na
   FROM pg_attribute AS a
   JOIN (
    SELECT nspname
     ,tbl.relname AS tblname
     ,idx.relname AS idxname
     ,idx.reltuples
     ,idx.relpages
     ,idx.relam
     ,indrelid
     ,indexrelid
     ,indkey::SMALLINT [] AS attnum
    FROM pg_index
    JOIN pg_class idx ON idx.oid = pg_index.indexrelid
    JOIN pg_class tbl ON tbl.oid = pg_index.indrelid
    JOIN pg_namespace ON pg_namespace.oid = idx.relnamespace
    WHERE pg_index.indisvalid
     AND tbl.relkind = 'r'
     AND pg_namespace.nspname NOT IN (
      'information_schema'
      ,'pg_catalog'
      )
    ) AS i ON a.attrelid = i.indexrelid
   JOIN pg_stats AS s ON s.schemaname = i.nspname
    AND (
     (
      s.tablename = i.tblname
      AND s.attname = pg_catalog.pg_get_indexdef(a.attrelid, a.attnum, TRUE)
      ) -- stats from tbl
     OR (
      s.tablename = i.idxname
      AND s.attname = a.attname
      )
     )
   JOIN pg_type AS t ON a.atttypid = t.oid
   WHERE a.attnum > 0
   GROUP BY 1
    ,2
    ,3
    ,4
    ,5
    ,6
    ,7
    ,8
    ,9
   ) AS s1
  ) AS s2
 JOIN pg_am am ON s2.relam = am.oid
 WHERE am.amname = 'btree'
 ) AS sub
ORDER BY 2
 ,3
 ,4;
"""

logging.basicConfig(level = logging.DEBUG)

def usage():
    print 'Usage ' + sys.argv[0] + ' [-H/--host] [-d/--dbname] [-u/--user] [-p/--password] [-o/--port] [-c/--critical] [-w/--warning] [-v/--verbose] [-h/--help]'
    print '\t -H Database server host to connect'
    print '\t -d Database to connect'
    print '\t -u DB user'
    print '\t -p DB password'
    print '\t -o DB port'
    print '\t -c Critical percent of bloating idx,table default is 80%,80%,52428800,1073741824'
    print '\t -w Warning percent of bloating idx,table default is 50%,50%,524288000,5368709120'
    print '\t -v Some verbose output'
    print '\t -h Print this help'
  
def parseArg():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'h:H:d:u:p:o:w:c:v:swsc', ["help", "file=", "host=", "dbname=", "user=", "password=", "port=", "warning=", "critical=", "verbose"])
    except getopt.GetoptError, err:
        print str(err)
        usage()
        sys.exit(2)

    global host
    global dbname
    global user
    global password
    global port
    global host
    global critical
    global warning
    global verbose
  
    for o, a in opts:
        if o in ("-v", "--verbose"):
            verbose = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-H", "--host"):
            host = a        
        elif o in ("-d", "--dbname"):
            dbname = a
        elif o in ("-u", "--user"):
            user = a
        elif o in ("-p", "--password"):
            password = a
        elif o in ("-o", "--port"):
            port = int(a)
        elif o in ("-c", "--critical"):
            critical = a
        elif o in ("-w", "--warning"):
            warning = a
        else:
            assert False, "unhandled option"
def parseThreashold( threashold ):
    thresholdList = threashold.split(",")
    for t in thresholdList:
        try:
          int(t)
        except ValueError:
          print "UNKNOWN: Invalid threshold input"
          sys.exit(1)
    return thresholdList
    
def dbQuery(query, user, password, dbname, host, port):
    try:
      conn = psycopg2.connect("host=%s port=%d dbname=%s user=%s password=%s" % ( host, port, dbname, user, password ))
      curs = conn.cursor()
      try:
        curs.execute(query)
        rows = curs.fetchall()
        curs.close()
        conn.close()
        return rows
      except StandardError, e:
        logging.error('Can''t execute query: %s' % query)
        if verbose: logging.error('Postgresql error code: %s' % e.pgcode)
        if verbose: logging.error('Postgresql error message: %s' % e.pgerror)
        curs.close()
        conn.close()
        sys.exit(1)
    except:
      logging.error('Can''t create DB connection')
      sys.exit(1)

def nagiosStringComposition( severityList, severityName ):
    if severityList:
        severityStr = ''
        for item in severityList:
            if ( item == severityList[-1] ):
                severityStr += item
            else:
                severityStr += item 
                severityStr += ','
        return severityName +': ' + severityStr
    else:
        if verbose: logging.debug('Empty severity list in nagiosStringComposition')
        print 'UNKNOWN'

def nagiosOutput( queryData ):
    warnList = []
    critList = []
    unknownList = []

    global warning
    global critical

    idxPercentWarn,tblPercentWarn,idxSizeWarn,tblSizeWarn = parseVars(warning)
    idxPercentCrit,tblPercentCrit,idxSizeCrit,tblSizeCrit = parseVars(critical)

    if queryData:
        for r in queryData:
            if ( warning <= float(r[4]) <= critical ):
                warnList.append(r[3])
            elif ( float(r[4]) > critical ):
                critList.append(r[3])
            else:
                unknownList.append(r[3])
    else:
        if verbose: logging.debug('Empty query result')
        print 'OK'
        return 0
  
    if critList:
         if verbose: logging.debug('Critical list: ' % critList)
         print nagiosStringComposition( critList, 'CRITICAL' )  
         return 2
    elif warnList:
         if verbose: logging.debug('Warning list: ' % warnList)
         print nagiosStringComposition( warnList, 'WARNING' )
         return 1
    elif unknownList:
         if verbose: logging.debug('Unknown list: ' % unknownList)
         print nagiosStringComposition( unknownList, 'UNKNOWN' )
         return 3
    else:
        if verbose: logging.debug('Unexpected values in query: %s' % readSqlFileName(file))
        print 'UNKNOWN'
        return 3

def main():
    parseArg()

    indexQuery = BloatIndexSQL()
    tableQuery = BloatTableSQL()

    global warning
    a,b,c,d = parseThreashold(warning)
    print a,b,c,d       

#    resList = dbQuery( indexQuery, user, password, dbname, host, port )
#    sys.exit ( nagiosOutput ( resList ) )

if __name__=='__main__':
    main()


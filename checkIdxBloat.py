#!/usr/bin/env python
import psycopg2
import logging
import getopt
import os
import sys

host = 'localhost'
dbname = 'database'
user = 'user'
password = 'password'
port = 5432
warning = '268435456,536870912'
critical = '1073741824,2147483648'
verbose = None
entity = 'index'

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

def usage():
    global warning
    global critical

    print 'Usage ' + sys.argv[0] + ' [-H/--host] [-d/--dbname] [-u/--user] [-p/--password] [-o/--port] [-c/--critical] [-w/--warning] [-e/--entity] [-v/--verbose] [-h/--help]'
    print '\t -H Database server host to connect'
    print '\t -d Database to connect'
    print '\t -u DB user'
    print '\t -p DB password'
    print '\t -o DB port'
    print '\t -c Critical size of bloating index,table, default is %s' % warning
    print '\t -w Warning size of bloating index,table, default is %s' %  critical
    print '\t -e Which entity check for bloat index or table, default is "index"'
    print '\t -v Some verbose output'
    print '\t -h Print this help'
  
def parseArg():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'h:H:d:u:p:o:w:c:e:v', ["help", "host=", "dbname=", "user=", "password=", "port=", "warning=", "critical=", "entity=", "verbose"])
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
    global entity
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
        elif o in ("-e", "--entity"):
            entity = a
        else:
            assert False, "unhandled option"

def parseThreashold( threashold ):
    thresholdList = threashold.split(",")
    
    if len(thresholdList) == 1:
        try:
            int(threashold)
            thresholdList.append(None)
            return thresholdList
        except:
            logging.debug('Threashold value: %s' % t)     
            print 'UNKNOWN: Invalid threshold value'
            sys.exit(3)
    else:
        for t in thresholdList:
            try:
                int(t)
            except ValueError:
                logging.debug('Threashold value: %s' % t)     
                print 'UNKNOWN: Invalid threshold value'
                sys.exit(3)
    
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
        print 'UNKNOWN: Can\'t execute query'
        logging.debug('Can\'t execute query: %s' % query)
        logging.debug('Postgresql error code: %s' % e.pgcode)
        logging.debug('Postgresql error message: %s' % e.pgerror)
        curs.close()
        conn.close()
        sys.exit(3)
    except Exception, e:
      print 'UNKNOWN: Can\'t create DB connection'
      logging.debug('Can\'t create DB connection\n' + str(e))
      sys.exit(3)

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
        logging.debug('Empty severity list in nagiosStringComposition')
        print 'UNKNOWN empty severity list'
        sys.exit(3)

def nagiosOutput(queryData):
    warnList = []
    critList = []
    okList = []

    global warning
    global critical
    global entity

    idxSizeWarn,tblSizeWarn = parseThreashold(warning)

    if not idxSizeWarn:
        idxSizeWarn = 268435456
    if not tblSizeWarn:
        tblSizeWarn = 536870912

    idxSizeCrit,tblSizeCrit = parseThreashold(critical)

    if not idxSizeCrit:
        idxSizeCrit = 1073741824
    if not tblSizeCrit:
        tblSizeCrit = 2147483648  

    if queryData:
        for r in queryData:
            if entity == 'index':
                if (int(idxSizeWarn) <= int(r[6]) < int(idxSizeCrit)):
                    warnList.append(r[3])
                elif (int(r[6]) >= int(idxSizeCrit)):
                    critList.append(r[3])
                else:
                    okList.append(r[3])
            elif entity == 'table':
                if (int(tblSizeWarn) <= int(r[6]) < int(tblSizeCrit)):
                    warnList.append(r[3])
                elif (int(r[6]) >= int(tblSizeCrit)):
                    critList.append(r[3])
                else:
                    okList.append(r[3])
            else:
                logging.debug('Entity type: %s' % entity)
                print 'UNKNOWN entity type'
                return 3

    else:
        print 'OK empty query result set'
        return 0
  
    if critList:
         logging.debug('Critical list: %s' % critList)
         print nagiosStringComposition( critList, 'CRITICAL' )  
         return 2
    elif warnList:
         logging.debug('Warning list: %s' % warnList)
         print nagiosStringComposition( warnList, 'WARNING' )
         return 1
    elif okList:
         logging.debug('OK list: %s' % okList)

         if entity.endswith('x'):
             print 'OK all %ses seems to be ok' % entity 
         else:
             print 'OK all %ss seems to be ok' % entity
         return 0

    else:
        logging.debug('All metrics is empty, check query: %s' % queryData)
        print 'UNKNOWN empty threashold list'
        return 3

def main():
    global entity
    global user
    global password
    global dbname
    global host
    global port
    global verbose

    parseArg()

    if verbose:
        logging.basicConfig(level = logging.DEBUG)
    else:
        logging.basicConfig(level = logging.INFO)

    indexQuery = BloatIndexSQL()
    tableQuery = BloatTableSQL()

    if entity == 'index':
        rowsList = dbQuery(indexQuery, user, password, dbname, host, 5433)
        sys.exit ( nagiosOutput ( rowsList ) )
    elif entity == 'table':
        rowsList = dbQuery(tableQuery, user, password, dbname, host, 5433)
        sys.exit ( nagiosOutput ( rowsList ) )
    else:
        logging.debug('Unknown entity type: %s' % entity)
        print 'UNKNOWN entity type'
        sys.exit(3)

if __name__=='__main__':
    main()

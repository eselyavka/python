#!/usr/bin/env python

import httplib, urllib, hashlib, re, logging, getopt, sys, os

def usage():
    print """%s, usage\n
              -h/--help - display this help\n
              <-r/--recepient> - recepient msisdn, could be string with comma separated values\n
              <-s/--subject> - subject\n
              <-b/--body> - text message\n
              """ % os.path.abspath(__file__) 

def checkNumber(msisdn):
    match = re.match(r'^7[0-9]{3}[0-9]{7}$', msisdn, re.M)
    if match:
        return True
    else:
        return False

def parseNumber(to):
    return to.split(",")

class SendSMS:
    """Class for sending email via http://smsaero.ru/api/"""

    url = "gate.smsaero.ru"
    port = 80
    user = "user"
    password = "password"

    logging.basicConfig(filename='/var/log/sendSMS/sendSMS.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)

    def __init__(self, to, subject, body):
        msisdns = parseNumber(to)
        for msisdn in msisdns:
            if checkNumber(msisdn):
                md5sum = hashlib.md5(SendSMS.password)
                params = urllib.urlencode({"user" : SendSMS.user, "password" : md5sum.hexdigest(), "to" : msisdn, "text" : body, "from" : "INFORM"})
                headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
                conn = httplib.HTTPConnection(SendSMS.url, SendSMS.port)
                conn.request("POST", "/send/", params, headers)
                res = conn.getresponse()
                data = res.read()
                if int(res.status) == 200 and res.reason == "OK":
                    match = re.match(r'[0-9]+\s*=\s*accepted', data, re.M|re.I)
                    if match:
                        logging.info("SMS sent: " + data)
                    else:
                        logging.info("SMS not sent: " + data)
                else:
                    logging.error("Server response: " + res.status + " and reason: " + res.reason)
                conn.close()
            else:
                logging.error("Check msisdn is correct: " + msisdn)

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"h:r:s:b:",["help","recepient=","subject=","body="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit(0)
        elif opt in ("-r", "--recepient"):
            recepient = arg
        elif opt in ("-s", "--subject"):
            subject = arg
        elif opt in ("-b", "--body"):
            body = arg
        else:
            assert False, "unhandled option" 
    
    if len(opts) < 3:
        usage()
        sys.exit(2)

    SendSMS(recepient, subject, body)

if __name__=='__main__':
    main(sys.argv[1:])

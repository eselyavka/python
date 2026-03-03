#!/usr/bin/env python3

"""AVRO integration helper script."""

# pylint: disable=wrong-import-order

import argparse
import logging
from pathlib import Path

try:
    import avro.schema
    from avro.datafile import DataFileReader, DataFileWriter
    from avro.io import DatumReader, DatumWriter
except ModuleNotFoundError as exc:
    raise SystemExit(
        "Missing Avro dependency. Install an Avro Python package before running this script."
    ) from exc

BASE_DIR = Path(__file__).resolve().parent
SCHEMA_PATH = BASE_DIR / "log.avsc"
DATA_PATH = BASE_DIR / "part-00000.avro"

with SCHEMA_PATH.open(encoding="utf-8") as schema_file:
    schema = avro.schema.parse(schema_file.read())


def writeFile():
    with DATA_PATH.open("wb") as output_file:
        writer = DataFileWriter(output_file, DatumWriter(), schema)
        writer.append({"logline": "2016\t30"})
        writer.close()


def sendData():
    from flumelogger import handler  # pylint: disable=import-outside-toplevel

    fh = handler.FlumeHandler(host='localhost', port=6666, type='ng', headers={'application': 'Skyline.Analyzer'})
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(fh)
    logger.info("python is cool")


#def sendFile():
#    client = ipc.HTTPTransceiver(server_addr[0], server_addr[1])
#    requestor = ipc.Requestor(PROTOCOL, client)
#
#    event = dict()
#
#    event['headers'] = {'name': 'abc', 'address': 'zyx'}
#    event['body'] = bytes('hello')
#
#    params = dict()
#
#    params['event'] = event
#
#    print("Result : " + requestor.request('append', params))
#
#    client.close()

def readFile():
    with DATA_PATH.open("rb") as input_file:
        reader = DataFileReader(input_file, DatumReader())
        for user in reader:
            print(user)
        reader.close()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--send", action="store_true", help="Send a sample log line to Flume.")
    args = parser.parse_args()

    if args.send:
        sendData()
    writeFile()
    readFile()

if __name__ == '__main__':
    main()

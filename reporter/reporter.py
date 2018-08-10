#!/usr/bin/env python2.7

import argparse
import logging
import os
import sys
import threading

import requests

from status_reporter.report import Report

NUM_THREADS = 5
LOG = logging.getLogger(__name__)
REPORT = Report()
SRV_TEMPLATE_URL = 'http://{server_name}.twitter.com/status'
NEED_ATTENTION_SRV = set()


def process_args():
    """
    Handle command line arguments

    Args:
        None
    Returns:
        None
    """
    parser = argparse.ArgumentParser(description='Request status of applications servers.')
    parser.add_argument('--input',
                        default='/tmp/input.txt',
                        help='input with list of servers')
    parser.add_argument('--output',
                        default='/tmp/output.tsv',
                        help='machine readable output')
    parser.add_argument('--debug',
                        action='store_true',
                        help='debug output')

    cli_args = parser.parse_args()

    return cli_args


def process_request(req):
    try:
        data = req.json()
        if ('Application' not in data or
                    'Version' not in data or
                    'Request_Count' not in data or
                    'Success_Count' not in data):
            raise StandardError("Invalid json format")

        REPORT.add(data['Application'],
                   data['Version'],
                   data['Request_Count'],
                   data['Success_Count'])
        return True
    except StandardError as err:
        LOG.debug(
            'Statistic data processing failed: (%s) %s',
            err.__class__.__name__,
            err
        )


def request_server(method,
                   req_url,
                   allow_redirects=False,
                   timeout=60,
                   **kwargs):

    LOG.debug('Requesting server: (%s) %s.', method, req_url)

    try:
        req = requests.request(
            method, req_url,
            allow_redirects=allow_redirects,
            timeout=timeout,
            **kwargs)

        LOG.debug(
            'Server returned: %d (%d bytes in %f sec)',
            req.status_code,
            len(req.content),
            req.elapsed.seconds + req.elapsed.microseconds / 10E+6)

        return req
    except (
            requests.exceptions.ConnectionError,
            requests.exceptions.HTTPError,
            requests.exceptions.TooManyRedirects,
            requests.exceptions.Timeout
    ) as err:
        LOG.debug(
            'Assuming server (%s) is unhealthy, caught: (%s) %s',
            req_url,
            err.__class__.__name__,
            err)


def requester(server_list):
    for srv in server_list:
        req = request_server('GET', SRV_TEMPLATE_URL.format(server_name=srv))
        if req is not None:
            res = process_request(req)
            if not res:
                NEED_ATTENTION_SRV.add(srv)
        else:
            NEED_ATTENTION_SRV.add(srv)


def executor(arr):
    tasks = []
    for i in range(NUM_THREADS):
        task = threading.Thread(target=requester, args=(arr[i],))
        tasks.append(task)
        task.start()

    [t.join() for t in tasks]


def report(output):
    print REPORT

    payload = REPORT.get_raw_storage()

    with open(output, 'w') as fh:
        fh.write('App\tVersion\tRate\n')
        for app in payload.keys():
            for ver in payload[app]:
                fh.write('{app}\t{ver}\t{rate:.4f}\n'.format(app=app,
                                                             ver=ver,
                                                             rate=payload[app][ver].rate()))

    LOG.info("Report successfully written to {}".format(output))


def read_and_split(input):
    with open(input, 'r') as fh:
        requires_processing = [x.strip() for x in fh.readlines()]

    if not requires_processing:
        return []

    batch_size = len(requires_processing) // NUM_THREADS

    i = 0
    work_set = []

    while i < NUM_THREADS:
        if i == NUM_THREADS - 1:
            work_set.append(requires_processing[i * batch_size:])
        else:
            work_set.append(requires_processing[i * batch_size: (i + 1) * batch_size])
        i += 1

    return work_set


def main(cli_args):
    logging_format = '\t'.join(
        ['%(asctime)s', '%(name)s', '%(levelname)s',
         '(%(process)d)', '(%(threadName)-10s)', '%(message)s'])
    logging.basicConfig(format=logging_format, level=logging.DEBUG if cli_args.debug else logging.INFO)

    if not os.path.isfile(cli_args.input):
        LOG.error("File {} doesn't exists".format(cli_args.input))
        sys.exit(1)

    work_set = read_and_split(cli_args.input)

    if work_set:
        executor(work_set)

    if NEED_ATTENTION_SRV:
        LOG.warning(
            "Those are the list of servers which requires maintenance=({})".format(','.join(NEED_ATTENTION_SRV)))

    report(cli_args.output)


if __name__ == '__main__':
    main(process_args())

#!/usr/bin/env python2.7

import os
import tempfile
import unittest

import mock
import requests

import reporter
from status_reporter.rate import SrvRate
from status_reporter.report import Report


class TestRate(unittest.TestCase):
    def test_server_rate_calculation(self):
        srv_rate = SrvRate(10, 4)
        srv_rate.add_total(5)
        srv_rate.add_succ(3)

        self.assertEqual(srv_rate.rate(), float(7) / float(15))

    def test_server_rate_calculation_with_zero_success(self):
        srv_rate = SrvRate(0, 4)

        self.assertEqual(srv_rate.rate(), float(0))


class TestReport(unittest.TestCase):
    def setUp(self):
        self.report = Report()

    def test_report_is_singelton(self):
        another_report = Report()
        self.assertEqual(id(self.report), id(another_report))

    def test_report_store(self):
        apps = ['app1', 'app2', 'app_zero']
        versions = ['1.0.0', '1.0.1']

        self.report.add(apps[0], versions[0], 10, 3)
        self.report.add(apps[0], versions[0], 10, 3)
        self.report.add(apps[1], versions[0], 10, 3)
        self.report.add(apps[1], versions[0], 10, 3)
        self.report.add(apps[1], versions[1], 100, 3)
        self.report.add(apps[1], versions[1], 14, 3)
        self.report.add(apps[2], versions[0], 0, 3)

        report_store = self.report.get_raw_storage()
        self.assertListEqual(sorted(report_store.keys()), sorted(apps))
        self.assertListEqual(report_store[apps[0]].keys(), [versions[0]])
        self.assertListEqual(report_store[apps[2]].keys(), [versions[0]])
        self.assertListEqual(report_store[apps[1]].keys(), versions)
        self.assertEqual(report_store[apps[0]][versions[0]].rate(), 0.3)
        self.assertEqual(report_store[apps[1]][versions[0]].rate(), 0.3)
        self.assertEqual(report_store[apps[1]][versions[1]].rate(), float(6) / float(114))
        self.assertEqual(report_store[apps[2]][versions[0]].rate(), 0.0)


class TestStatusReport(unittest.TestCase):
    def setUp(self):
        self.method = 'GET'
        self.url = 'http://example.com'

    def test_process_args_should_set_defaults(self):
        args = reporter.process_args()
        self.assertFalse(args.debug)
        self.assertTrue(args.input)
        self.assertTrue(args.output)

    def test_process_request_should_return_false_on_invalid_json(self):
        req = mock.MagicMock(**{'json.return_value': {'invalid': True}})
        self.assertFalse(reporter.process_request(req))

    def test_process_request_should_return_true_on_valid_json(self):
        app = 'app3'
        ver = '1.0.0'
        req = mock.MagicMock(**{'json.return_value': {'Application': app,
                                                      'Version': ver,
                                                      'Request_Count': 100,
                                                      'Success_Count': 9}})
        self.assertTrue(reporter.process_request(req))
        self.assertEqual(reporter.REPORT.get_raw_storage()[app][ver].rate(), float(9) / float(100))

    def test_request_sever_should_return_false_on_requests_exception(self):
        with mock.patch('reporter.requests.request') as mock_requests:
            mock_requests.side_effect = requests.exceptions.HTTPError('unittest')
            self.assertFalse(reporter.request_server(self.method, self.url))

    def test_request_sever_should_return_request_instance_on_success(self):
        with mock.patch('reporter.requests.request') as mock_requests:
            mock_requests.return_value = mock.MagicMock(**{'status_code': 200})
            self.assertTrue(reporter.request_server(self.method, self.url))
            self.assertTrue(mock.call(self.method,
                                      self.url,
                                      allow_redirects=False,
                                      timeout=60) in mock_requests.mock_calls)

    def test_requester_should_populate_need_attention_set_when_error_in_request_server(self):
        apps = ['app1', 'app2']
        with mock.patch('reporter.request_server') as mock_request_server:
            mock_request_server.return_value = None
            reporter.requester(apps)
            self.assertSetEqual(reporter.NEED_ATTENTION_SRV, set(apps))

    def test_requester_should_populate_need_attention_set_when_error_in_process_request(self):
        apps = ['app1', 'app2']
        with mock.patch('reporter.request_server') as mock_request_server:
            mock_request_server.return_value = True
            with mock.patch('reporter.process_request') as mock_process_request:
                mock_process_request.return_value = None
                reporter.requester(apps)
                self.assertSetEqual(reporter.NEED_ATTENTION_SRV, set(apps))

    def test_report_write_to_file(self):
        with tempfile.NamedTemporaryFile() as fh:
            reporter.report(fh.name)
            self.assertTrue(os.path.exists(fh.name))
            self.assertTrue(os.stat(fh.name).st_size > 0)

    def test_read_and_split_should_return_empty_list_on_no_input(self):
        with tempfile.NamedTemporaryFile() as fh:
            res = reporter.read_and_split(fh.name)
            self.assertListEqual(res, [])

    @staticmethod
    def read_input_srv_list(app_srvs):
        with tempfile.NamedTemporaryFile() as fh:
            fh.writelines(app_srvs)
            fh.flush()
            split_servers = reporter.read_and_split(fh.name)

        return split_servers

    def test_read_and_split_should_return_list_when_input(self):
        app_srvs = ['app{}\n'.format(x) for x in range(1, 6)]
        self.assertListEqual(TestStatusReport.read_input_srv_list(app_srvs),
                             [[srv.strip()] for srv in app_srvs])

        app_srvs = ['app{}\n'.format(x) for x in range(1, 7)]
        self.assertTrue([len(x) in [1, 2] for x in TestStatusReport.read_input_srv_list(app_srvs)])

        app_srvs = ['app{}\n'.format(x) for x in range(1, 1001)]
        self.assertTrue(all([len(x) == 200 for x in TestStatusReport.read_input_srv_list(app_srvs)]))

        app_srvs = ['app{}\n'.format(x) for x in range(1, 1029)]
        self.assertTrue([len(x) in [205, 208] for x in TestStatusReport.read_input_srv_list(app_srvs)])


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python3

"""Module for projects.reporter.status_reporter.report."""

from .rate import SrvRate


class Report(object):
    __report = None

    def __init__(self):
        self._store = {}

    def __new__(cls):
        if Report.__report is None:
            Report.__report = object.__new__(cls)
        return Report.__report

    def add(self, app, version, total, succ):
        if app not in self._store:
            self._store[app] = {version: SrvRate(total=total, succ=succ)}
        else:
            _app = self._store[app]
            if version in _app:
                _app[version].add_total(total)
                _app[version].add_succ(succ)
                return
            _app.update({version: SrvRate(total=total, succ=succ)})

    def get_raw_storage(self):
        return self._store

    def __str__(self):
        report = 'Summary report for app servers status:\n\n'
        for app in self._store:
            report += f"Application '{app}'\n"
            for ver in self._store[app]:
                report += f"\t\tVersion='{ver}', success rate is '{self._store[app][ver].rate():.4f}'\n"
            report += '\n\n'
        return report

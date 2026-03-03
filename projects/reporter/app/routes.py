#!/usr/bin/env python3

"""Module for projects.reporter.app.routes."""

import random

from flask import jsonify, request

from . import app

@app.route('/')
@app.route('/status')
def index():
    apps = ['db', 'cache', 'web']
    rnd_str = ''
    host = list(request.headers['Host'])
    for _ in host:
        rnd_str += random.choice(host)

    request_index = app.config.setdefault("REQUEST_INDEX", 0)
    _hash = 0 if request_index and request_index % 10 == 0 else hash(rnd_str)

    def rnd(postfix=None):
        return str(random.randint(1, 9)) + (postfix if postfix else '')

    app.config["REQUEST_INDEX"] = request_index + 1

    return jsonify({"Application": random.choice(apps),
                    "Version": rnd('.') + rnd('.') + rnd(),
                    "Request_Count": _hash / random.randint(100000, 1000000),
                    "Success_Count": _hash / random.randint(1000000, 2000000)})

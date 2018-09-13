import random

from flask import jsonify, request

from app import app


@app.route('/')
@app.route('/status')
def index():
    apps = ['db', 'cache', 'web']
    rnd_str = ''
    host = list(request.headers['Host'])
    for _ in host:
        rnd_str += random.choice(host)
    _hash = hash(rnd_str)
    random.choice(apps)

    def rnd(postfix=None):
        return str(random.randint(1, 9)) + (postfix if postfix else '')

    return jsonify({"Application": random.choice(apps),
                    "Version": rnd('.') + rnd('.') + rnd(),
                    "Request_Count": _hash / random.randint(100000, 1000000),
                    "Success_Count": _hash / random.randint(1000000, 2000000)})

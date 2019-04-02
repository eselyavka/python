import random

from flask import jsonify, request

from app import app

idx = 0

@app.route('/')
@app.route('/status')
def index():
    global idx
    apps = ['db', 'cache', 'web']
    rnd_str = ''
    host = list(request.headers['Host'])
    for _ in host:
        rnd_str += random.choice(host)

    _hash = 0 if idx and idx % 10 == 0 else hash(rnd_str)

    def rnd(postfix=None):
        return str(random.randint(1, 9)) + (postfix if postfix else '')

    idx += 1

    return jsonify({"Application": random.choice(apps),
                    "Version": rnd('.') + rnd('.') + rnd(),
                    "Request_Count": _hash / random.randint(100000, 1000000),
                    "Success_Count": _hash / random.randint(1000000, 2000000)})

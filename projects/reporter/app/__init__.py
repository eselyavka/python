#!/usr/bin/env python3

"""Reporter Flask app package."""

# Importing routes after app creation is intentional.
# pylint: disable=wrong-import-position,cyclic-import

from flask import Flask

app = Flask(__name__)

from . import routes

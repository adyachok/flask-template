#!/usr/bin/env python
import logging

import coloredlogs as coloredlogs
from flask import Flask, jsonify

from blueprints.ds import ds
from config import get_config_object


app = Flask(__name__)
app.config.from_object(get_config_object())
logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG')


@app.route('/', methods=['GET'])
def welcome():
    return jsonify({'msg': 'Ok'}), 200


app.register_blueprint(ds,
                       url_prefix=f'{app.config["APPLICATION_ROOT"]}/ds')


# local development ($ python main.py)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

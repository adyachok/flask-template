import logging

import coloredlogs
from flask import Blueprint, jsonify

from config import DefaultConfig


ds = Blueprint('ds', __name__)
conf = DefaultConfig()
logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG')


@ds.route('/', methods=['GET'])
def hello():
    return jsonify({'msg': 'Hello from ds'})

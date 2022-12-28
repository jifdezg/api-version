from flask import Blueprint

import common

api = Blueprint("api", __name__)

@api.route("/clients")
def get_clients():
    return common.get_clients()

@api.route("/services")
def get_services():
    return "output 1 (v1)"

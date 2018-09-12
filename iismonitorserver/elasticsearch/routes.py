from flask import Blueprint, request
import json

es_api = Blueprint('es_api', __name__)

@es_api.route('/services', methods=['POST'])
def register_servicelog():
    return json.dumps(request.json)
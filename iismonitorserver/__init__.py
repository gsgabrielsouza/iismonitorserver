from flask import Flask, Blueprint

app = Flask(__name__)

from iismonitorserver.elasticsearch.routes import es_api

app.register_blueprint(es_api, url_prefix='/es')
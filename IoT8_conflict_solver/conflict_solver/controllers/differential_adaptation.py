from flask import make_response
from flask_restful import Resource

from models.model import DifferentialAdaptation
import json

class DifferentialAdaptationController(Resource):

    def get(self):
        das = DifferentialAdaptation().findAll()
        #das = assembleDifferentialAdaptations()
        resp = make_response(json.dumps(das))
        resp.headers['content-type'] = 'application/json'

        return resp

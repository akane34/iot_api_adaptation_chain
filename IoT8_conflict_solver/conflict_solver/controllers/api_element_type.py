from flask import make_response
from flask_restful import Resource

import json
from models.model import ApiElementType

class ApiElementTypeController(Resource):

    def get(self):
        types = ApiElementType().findAll()
        resp = make_response(json.dumps(types))
        resp.headers['content-type'] = 'application/json'
        return resp


from flask import make_response
from flask_restful import Resource

import json
from models.model import AdaptationNode

class AdaptationNodeController(Resource):

    def get(self):
        nodes = AdaptationNode().findAll()
        resp = make_response(json.dumps(nodes))
        resp.headers['content-type'] = 'application/json'
        return resp


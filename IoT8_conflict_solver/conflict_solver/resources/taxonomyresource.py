from flask import make_response
from flask_restful import Resource

import json
from models.model import Taxonomy

class TaxonomyResource(Resource):

    def get(self):
        taxonomies = Taxonomy().findAll()
        resp = make_response(json.dumps(taxonomies))
        resp.headers['content-type'] = 'application/json'
        return resp


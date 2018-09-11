from flask import request, make_response
from flask_restful import Resource


import requests

from services import adaptation

class Routing(Resource):

    def get(self, url):
        apiname, apiresource =\
                    adaptation.splitApiNameApiResource(url) 
        adaptations = adaptation.getAdaptations(
                    apiname, apiresource) 
        response = adaptation.runAdaptations(
                'GET', url, adaptations)

        resp = make_response(response.text)
        resp.headers['content-type'] = 'application/json'
        return resp

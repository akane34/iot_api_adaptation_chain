from flask import request, make_response
from flask_restful import Resource

import json
from models.model import Differential
from models.differentials import ApiDifferential, ElementDifferential,\
        Differential as DiffRep
from services.api_element import apiElementTypeFromElementPath,\
        apiResourceFromElementPath, differentialTimingFromElementPath
from services.differential_adaptation import adaptDifferentials


class DifferentialResource(Resource):

    def get(self):
        diffs = Differential().findAll()
        resp = make_response(json.dumps(diffs))
        resp.headers['content-type'] = 'application/json'
        return resp

    def post(self):
        itemJSON = request.get_json(force=True)
        itemObj = json.fromJSON(ApiDifferential, itemJSON) 
        diffs = []
        for diff in itemObj.element_differentials:
            element_differential = json.fromJSON(ElementDifferential, diff)
            diffRep = DiffRep.fromDifferentials(itemObj,
                    element_differential)
            diffRep.DifferentialTimingID = \
                    differentialTimingFromElementPath(diffRep.ElementPath).value
            diffRep.ApiResource = \
                    apiResourceFromElementPath(diffRep.ElementPath)
            diffRep.ApiElementTypeID = \
                    apiElementTypeFromElementPath(diffRep.ElementPath).value

            diffs.append(diffRep)

        query = Differential.save(diffs)
        adaptDifferentials()
        return


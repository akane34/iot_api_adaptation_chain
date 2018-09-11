from flask import request
from flask_jsonpify import jsonify
from flask_restful import Resource, reqparse

from services import caster

class Caster(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('value', location='json')
        parser.add_argument('to-type', location='json')

        args = parser.parse_args()
        value = args['value'].encode('utf-8').strip()
        toType = args['toType'].encode('utf-8').strip()

        newValue = caster.cast(value, toType)
        print('\t* Conversion of value {} to type {} resulted {}'
                .format(value, toType, newValue))

        return jsonify({'type': toType, 'value': newValue})

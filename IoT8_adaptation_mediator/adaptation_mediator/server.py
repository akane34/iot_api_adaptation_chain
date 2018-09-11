from flask import Flask
from flask_restful import Api


class Server():

    def __init__( self, port):
        self.port = port
        self.app = Flask(__name__)
        self.api = Api(self.app)

    def serve(self):
        self.app.run(host='0.0.0.0', port=self.port)

    def addResource(self, res):
        if not type(res) is tuple or len(res) < 2:
            raise Exception('Invalid resource container...')
        self.api.add_resource(res[0], [1])

    def addResources(self, resources):
        if not type(resources) is list:
            raise Exception('Invalid resource container...')

        for res in resources:
            if not type(res) is tuple or len(res) < 2:
                raise Exception('Invalid resource container...')
            print('Adding resource {} to path {}'.format(res[0], res[1]))
            self.api.add_resource(res[0], res[1])


from flask import Flask
from flask_restful import Api


class Server():

    def __init__( self, port):
        self.port = port
        self.app = Flask(__name__)
        self.api = Api(self.app)

    def serve(self):
        self.app.run(host='0.0.0.0', port=self.port)

    def addController(self, controller):
        if not type(controller) is tuple or len(controller) < 2:
            raise Exception('Invalid resource container...')
        self.api.add_resource(controller[0], [1])

    def addControllers(self, controllers):
        if not type(controllers) is list:
            raise Exception('Invalid resource container...')

        for res in controllers:
            if not type(res) is tuple or len(res) < 2:
                raise Exception('Invalid resource container...')
            print('Adding resource {} to path {}'.format(res[0], res[1]))
            self.api.add_resource(res[0], res[1])


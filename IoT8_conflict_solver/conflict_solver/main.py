import os
from server import Server
from server import app
from resources.differentials import DifferentialResource
from resources.taxonomyresource import TaxonomyResource
from resources.adaptation_node import AdaptationNodeResource
from resources.differential_adaptation import DifferentialAdaptationResource
from resources.api_element_type import ApiElementTypeResource

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///conflict_solver.db'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

def main():
    print('*************************************')
    print('          CONFLICT SOLVER')
    print('*************************************')

    print('Reading settings...')
    port = int(os.getenv(key='CONFLICT_SOLVER_PORT') or "5000")

    print('Initiating server')
    server = Server(port=port)

    print('Loading resources')
    server.addResources([
            (DifferentialResource, '/differential'),
            (TaxonomyResource, '/taxonomy'),
            (AdaptationNodeResource, '/adaptation'),
            (DifferentialAdaptationResource, '/differential_adaptation'),
            (ApiElementTypeResource, '/api_element_type')
        ])

    print('Starting server')
    server.serve()

if __name__ == '__main__':
    main()
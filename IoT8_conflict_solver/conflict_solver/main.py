import os
from server import Server
from server import app
from controllers.differentials import DifferentialController
from controllers.taxonomy import TaxonomyController
from controllers.adaptation_node import AdaptationNodeController
from controllers.differential_adaptation import DifferentialAdaptationController
from controllers.api_element_type import ApiElementTypeController

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///conflict_solver.db'

def main():
    print('*************************************')
    print('          CONFLICT SOLVER')
    print('*************************************')

    print('Reading settings...')
    port = 5000
    if os.getenv("CONFLICT_SOLVER_PORT") is not None:
        port = int(os.getenv("CONFLICT_SOLVER_PORT"))

    print('Initiating server')
    server = Server(port=port)

    print('Loading controllers')
    server.addControllers([
            (DifferentialController, '/differential'),
            (TaxonomyController, '/taxonomy'),
            (AdaptationNodeController, '/adaptation'),
            (DifferentialAdaptationController, '/differential_adaptation'),
            (ApiElementTypeController, '/api_element_type')
        ])

    print('Starting server')
    server.serve()

if __name__ == '__main__':
    main()
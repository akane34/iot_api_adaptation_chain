import os


from server import Server
from resources.routing import Routing


def main():
    print('*************************************')
    print('        ADAPTATION MEDIATOR')
    print('*************************************')
    
    print('Reading settings...')
    #port = int(os.getenv(key='ADAPTATION_MEDIATOR_PORT' or 4900))
    port = 4900
    conflictSolverUrl = str(os.getenv(key='CONFLICT_SOLVER_URL'))
    adaptationChainUrl = str(os.getenv(key='ADAPTATION_CHAIN_URL'))

    print('Initiating server...')
    server = Server(port=port)

    print('Loading resources...')
    server.addResources([
        (Routing, '/<path:url>')
            ])

    print('Starting server...')
    server.serve()

if __name__ == '__main__':
    main()

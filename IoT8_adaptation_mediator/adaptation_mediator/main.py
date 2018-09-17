import os
from server import Server
from controllers.routing import Routing

def main():
    print('*************************************')
    print('        ADAPTATION MEDIATOR')
    print('*************************************')
    
    print('Reading settings...')
    port = 4900
    if os.getenv("ADAPTATION_MEDIATOR_PORT") is not None:
        port = int(os.getenv("ADAPTATION_MEDIATOR_PORT"))

    print('Initiating server...')
    server = Server(port=port)

    print('Loading controllers...')
    server.addControllers([
        (Routing, '/<path:url>')
            ])

    print('Starting server...')
    server.serve()

if __name__ == '__main__':
    main()

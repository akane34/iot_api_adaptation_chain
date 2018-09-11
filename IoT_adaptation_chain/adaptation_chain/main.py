import os

from server import Server
from resources.caster import Caster

def main():
    print('*************************************')
    print('         ADAPTATION CHAIN')
    print('*************************************')
    
    print('Reading settings...')
    #port = int(os.getenv(key='ADAPTATION_CHAIN_PORT' or 4950))
    port = 4950
    print('Initiating server...')
    server = Server(port=port)

    print('Loading resources...')
    server.addResources([
        (Caster, '/caster')
            ])

    print('Starting server...')
    server.serve()

if __name__ == '__main__':
    main()

import sys, os, json
import settings
from httpinterface import get, post
from services.comparer import processApis 

settings.init()

def main():
    args = sys.argv
    postContent = False
    
    if len(args) < 3:
        print('Requires API v1 and API v2 paths for comparisson')
        return 2

    if len(args) > 3:
        postContent = boolParse(args[3])

    path_api1 = args[1]
    path_api2 = args[2]

    differential = processApis(path_api1, path_api2)

    differentialAsJson = json.loads(differential.toJSON())
    payload = differentialAsJson['element_differentials']

    if not postContent:
        print(differential.toJSON())
        return 0

    if postContent:
        conflict_uri = '{}/differential'.format(settings.CONFLICT_SOLVER_URL)
        print('-Delivering data to server {}\n{}\n'.format(conflict_uri, differentialAsJson))

        response = post(
            conflict_uri,
            data=None,
            json=differentialAsJson,
        )
        print('-Received \n{}\n'.format(response.json))


def boolParse(v):
    return v.lower() in ("yes", "true", "t", "1", "y")

if __name__ == '__main__':
    main()

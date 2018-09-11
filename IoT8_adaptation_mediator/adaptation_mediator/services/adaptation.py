import os, json
import requests 

from models.adaptation import Adaptation


def getAdaptations(apiname, apiresource):
    conflictSolverUrl = os.getenv(key='CONFLICT_SOLVER_URL')
    response = requests.put(
            '{}/adaptation'.format(
                    conflictSolverUrl),
                    json={'ApiName': apiname,
                    'ApiResource': apiresource},
            )
    jsonArr = response.json()

    adaptations = []
    for obj in jsonArr:
        adaptation = Adaptation()
        for field, value in obj.iteritems():
            setattr(adaptation, field, value) 
        adaptations.append(adaptation)

    return adaptations


def splitApiNameApiResource(url):
    separator = url.find('/')
    apiname = url[:separator]
    apiresource = url[separator + 1:]

    return apiname, apiresource


def runAdaptations(verb, url, adaptations, request=None):
    
    adaptationChainUrl = os.getenv(key='ADAPTATION_CHAIN_URL')
    requestAdaptations = []
    responseAdaptations = []

    response = None
    
    for adaptation in adaptations:
        if adaptation.MessageFlow.upper() == 'RESPONSE':
            responseAdaptations.append(adaptation)
        else:
            requestAdaptations.append(adaptation) 
    
    for adaptation in requestAdaptations:
        runRequestAdaptation(url, adaptation, request)

    response = doRequest(verb, url, request)

    for adaptation in responseAdaptations: 
        runResponseAdaptation(url, adaptation, request)

    return response


def runRequestAdaptation(url, adaptation, request=None):
    print('\tRunning request navigation...')


def runResponseAdaptation(url, adaptation, request=None):
    print('\tRunning response adaptation ...')
    print('{}'.format(dir(adaptation)))


def doRequest(verb, url, request=None):
    response = None
    httpVerb = verb.upper()

    if httpVerb == 'POST':
        print('\tDoing post...')
    else:
        response = requests.get(
                    'http://{}'.format(url),
                )

    return response

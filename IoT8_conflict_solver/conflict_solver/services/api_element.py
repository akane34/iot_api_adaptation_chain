import re
from enum import Enum

EXP = "{}{}{}{}{}{}{}".format(
        '\s*(?:',
        '(paths|requestBody|responses|content|schema|items|properties|type)|',  # 1 Key Word
        '([/][a-zA-Z0-9_/?=]+)|',   # 2 Resource
        '([a-zA-Z0-9_/]+)|',        # 3 Value
        '(\{[a-zA-Z0-9]+\})|',      # 4 Parameter
        '(.)',                      # 5 Undefined
        ')'
)

"""
Analyzes lexical items in the input path
"""
def parsePath(path):
    pattern = re.compile(EXP)
    scan = pattern.scanner(path)
    pathItems = []

    while 1:
        m = scan.match()
        if not m:
            break

        index = m.lastindex
        if not ElementPathToken(index) == ElementPathToken.UNDEFINED:
            pathItems.append((ElementPathToken(index), m.group(index)))

    return pathItems


"""
Determines the element type from the input path
"""
def apiElementTypeFromElementPath(element_path):
    pathItems = parsePath(element_path)
   
    for item in reversed(pathItems):
        if item[0] == ElementPathToken.UNDEFINED or \
                item[0] == ElementPathToken.VALUE:
            continue

        if item[0] == ElementPathToken.KEY_WORD:
            elementToken = str(item[1]).upper()
            if elementToken == 'TYPE':
                return ApiElementType.PROPERTY_TYPE
            if elementToken == 'PROPERTIES':
                return ApiElementType.PROPERTY_NAME
            else:
                return ApiElementType.UNDEFINED

    return ApiElementType.UNDEFINED


"""
Determines the API resource from the input path
"""
def apiResourceFromElementPath(element_path):
    pathItems = parsePath(element_path)
    apiResourcePath = '' 
    for item in pathItems:
        elementToken = item[0]
        elementValue = item[1]
        
        if elementToken == ElementPathToken.KEY_WORD and\
                str(elementValue).upper() == 'PATHS':
            continue 

        if elementToken == ElementPathToken.RESOURCE or\
                elementToken == ElementPathToken.PARAMETER:
            apiResourcePath += elementValue
            continue 

        break

    return apiResourcePath


def differentialTimingFromElementPath(element_path):
    pathItems = parsePath(element_path)

    for item in pathItems:
        elementToken = item[0]
        elementValue = item[1]
        if not elementToken == ElementPathToken.KEY_WORD:
            continue

        if str(elementValue).upper() == 'REQUESTBODY':
            return DifferentialTiming.REQUEST
        elif str(elementValue).upper() == 'RESPONSES':
            return DifferentialTiming.RESPONSE

    return DifferentialTiming.UNDEFINED


"""
Defines the values mapped for Tokens in the ElementPath
"""
class ElementPathToken(Enum):
    KEY_WORD=1
    RESOURCE=2
    VALUE=3
    PARAMETER=4
    UNDEFINED=5


"""
Defines the values mapped for ApiElements
"""
class ApiElementType(Enum):
    PROPERTY_TYPE = 1
    PROPERTY_NAME = 2
    UNDEFINED = -1


"""
Describes the differential timing: Request || Response
"""
class DifferentialTiming(Enum):
    REQUEST = 1
    RESPONSE = 2
    UNDEFINED = -1

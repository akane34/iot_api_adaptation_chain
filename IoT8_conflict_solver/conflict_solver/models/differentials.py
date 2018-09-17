import re
from enum import Enum
from models.model import Differential as DifferentialModel

"""
Describes a batch of differences between two APIs
"""
class ApiDifferential(): 

    def __init__(self,
                api_name='',
                api_server='',
                api_old_version='',
                api_new_version='',
                element_differentials=[]
            ):

        self.api_name = api_name
        self.api_server = api_server
        self.api_old_version = api_old_version
        self.api_new_version = api_new_version
        self.element_differentials = element_differentials

    def addElementDifferential(self, diff):
        self.element_differentials.append(diff)

    def fromJson(self, itemJson):
        apiDifferential = ApiDifferential()
        apiDifferential.api_name = itemJson['api_name']
        apiDifferential.api_server = itemJson['api_server']
        apiDifferential.api_old_version = itemJson['api_old_version']
        apiDifferential.api_new_version = itemJson['api_new_version']

        elementDifferentials = []
        for element in itemJson['element_differentials']:
            x = ElementDifferential()
            x.differential_type = element['differential_type']
            x.new_element = element['new_element']
            x.old_element = element['old_element']

            paths = []
            for path in element['element_path']:
                paths.append(path)
            x.element_path = paths

            elementDifferentials.append(x)
        apiDifferential.element_differentials = elementDifferentials

        return apiDifferential;

"""
Describes a single atomic difference between two APIs at the element level
"""
class ElementDifferential():

    def __init__(self,
                differential_type=3,
                element_path='',
                old_element='',
                new_element=''
            ):
        self.differential_type = differential_type
        self.element_path = element_path
        self.old_element = old_element
        self.new_element = new_element


"""
Defines the interface model against the data repository
"""
class Differential():

    def __init__(self,
            DifferentialID=0,
            ApiName='',
            ApiServer='',
            ApiOldVersion='',
            ApiNewVersion='',
            ElementPath='',
            DifferentialTypeID=3,       # Add=1, Delete=2, Modify=3
            DifferentialTimingID=-1,    # Request=1, Response=2, Undefined=-1
            OldElement='',
            NewElement='',
            ApiResource='',             # Calculated from API paths
            ApiElementTypeID=0):        # Calculated from ElementPath

        self.DifferentialID = DifferentialID
        self.ApiName = ApiName
        self.ApiServer = ApiServer
        self.ApiOldVersion = ApiOldVersion
        self.ApiNewVersion = ApiNewVersion
        self.ElementPath = ElementPath
        self.DifferentialTypeID = DifferentialTypeID
        self.DifferentialTimingID = DifferentialTimingID
        self.OldElement = OldElement
        self.NewElement = NewElement
        self.ApiResource = ApiResource
        self.ApiElementTypeID = ApiElementTypeID

        if not self.DifferentialID > 0:
            delattr(self, 'DifferentialID')

    @staticmethod
    def fromDifferentials(api_differential, element_differential):

        element_path = ''.join(str(item) + ',' for item in
                element_differential.element_path)
        element_path = element_path[:len(element_path)-1]

        return DifferentialModel(
                    ApiName=api_differential.api_name,
                    ApiServer=api_differential.api_server,
                    ApiOldVersion=api_differential.api_old_version,
                    ApiNewVersion=api_differential.api_new_version,
                    ElementPath=element_path,
                    DifferentialTypeID=element_differential.differential_type,
                    OldElement=element_differential.old_element,
                    NewElement=element_differential.new_element,
                )


"""
Defines the values allowed for element differential types
"""
class DifferentialType(Enum):
    ADD = 1
    DELETE = 2
    MODIFY = 3

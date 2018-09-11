"""
Describes realtionship between a differential an its adaptation
"""
class DifferentialAdaptation():

    def __init__(self,
                DifferentialAdaptationID=0,
                DifferentialID=0,
                AdaptationNodeID=0,
                ApiServer='',
                ApiResource='',
                AdaptationNodeVerb='',
                AdaptationNodePath='',
                AdaptationNodeRequest='',
                AdaptationNodeResponse='',
                DifferentialTypeID=-1,
                DifferentialTimingID=-1,
                ElementPath='',
                OldElement='',
                NewElement='',
                ApiOldVersion='',
                ApiNewVersion='',
            ):

        self.DifferentialAdaptationID = DifferentialAdaptationID
        self.DifferentialID = DifferentialID
        self.AdaptationNodeID = AdaptationNodeID
        self.ApiServer = ApiServer
        self.ApiResource = ApiResource
        self.AdaptationNodeVerb = AdaptationNodeVerb
        self.AdaptationNodePath = AdaptationNodePath
        self.AdaptationNodeRequest = AdaptationNodeRequest
        self.AdaptationNodeResponse = AdaptationNodeResponse
        self.DifferentialTypeID = DifferentialTypeID
        self.DifferentialTimingID = DifferentialTimingID
        self.ElementPath = ElementPath
        self.OldElement = OldElement
        self.NewElement = NewElement
        self.ApiOldVersion = ApiOldVersion
        self.ApiNewVersion = ApiNewVersion

        if not self.DifferentialAdaptationID > 0:
            delattr(self, 'DifferentialAdaptationID') 


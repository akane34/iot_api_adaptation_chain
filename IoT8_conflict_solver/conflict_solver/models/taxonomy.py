class Taxonomy():

    def __init__(self,
                TaxonomyID=0,
                Description='',
                DifferentialTypeID=0,
                ApiElementTypeID=0,
                AdaptationNodeID=0,
            ):

        self.TaxonomyID = TaxonomyID
        self.Description = Description
        self.DifferentialTypeID = DifferentialTypeID
        self.ApiElementTypeID = ApiElementTypeID
        self.AdaptationNodeID = AdaptationNodeID

        if not TaxonomyID > 0:
            delattr(self, 'TaxonomyID')

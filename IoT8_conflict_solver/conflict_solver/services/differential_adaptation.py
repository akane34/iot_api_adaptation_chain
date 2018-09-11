from models.model import DifferentialAdaptation

ADAPT_DIFFERENTIALS_QUERY = "\
        INSERT INTO DifferentialAdaptation(\
                DifferentialID,\
                AdaptationNodeID,\
                ApiServer,\
                ApiResource,\
                AdaptationNodeVerb,\
                AdaptationNodePath,\
                AdaptationNodeRequest,\
                AdaptationNodeResponse,\
                DifferentialTypeID,\
                DifferentialTimingID,\
                ElementPath,\
                OldElement,\
                NewElement,\
                ApiOldVersion,\
                ApiNewVersion\
            )\
        SELECT D.DifferentialID,\
                AN.AdaptationNodeID,\
                D.ApiServer,\
                D.ApiResource,\
                AN.AdaptationNodeVerb,\
                AN.AdaptationNodePath,\
                AN.AdaptationNodeRequest,\
                AN.AdaptationNodeResponse,\
                D.DifferentialTypeID,\
                D.DifferentialTimingID,\
                D.ElementPath,\
                D.OldElement,\
                D.NewElement,\
                D.ApiOldVersion,\
                D.ApiNewVersion\
        FROM Differential D\
        INNER JOIN Taxonomy T\
            ON D.DifferentialTypeID = T.DifferentialTypeID\
            AND D.DifferentialTimingID = T.DifferentialTimingID\
            AND D.ApiElementTypeID = T.ApiElementTypeID\
        INNER JOIN AdaptationNode AN\
            ON T.AdaptationNodeID = AN.AdaptationNodeID\
        LEFT JOIN DifferentialAdaptation DA\
            ON D.DifferentialID = DA.DifferentialID\
        WHERE DA.DifferentialID IS NULL;"


"""
Attempts to solve api differentials by searching for compatible nodes
described in the taxonomy table
"""
def adaptDifferentials():
    DifferentialAdaptation.executeInsert(ADAPT_DIFFERENTIALS_QUERY)

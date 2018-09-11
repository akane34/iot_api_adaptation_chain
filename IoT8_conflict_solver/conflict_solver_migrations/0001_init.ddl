/**
*   ApiElementType
*/
DROP TABLE IF EXISTS ApiElementType;
CREATE TABLE ApiElementType (
    ApiElementTypeID INTEGER PRIMARY KEY,
    ApiElementTypeName VARCHAR(500),
    ApiElementTypeDescription VARCHAR(500)
);


/**
*   DifferentialType
*/
DROP TABLE IF EXISTS DifferentialType;
CREATE TABLE DifferentialType (
    DifferentialTypeID INTEGER PRIMARY KEY,
    DifferentialTypeDescription VARCHAR(500)
);


/**
*   DifferentialTiming
*/
DROP TABLE IF EXISTS DifferentialTiming;
CREATE TABLE DifferentialTiming (
    DifferentialTimingID INTEGER PRIMARY KEY,
    DifferentialTimingName VARCHAR(100),
    DifferentialTimingDescription VARCHAR(500)
);


/**
*   Differential
*/
DROP TABLE IF EXISTS Differential;
CREATE TABLE Differential (
    DifferentialID INTEGER PRIMARY KEY,
    ApiName VARCHAR(500),
    ApiServer VARCHAR(500),
    ApiOldVersion VARCHAR(50),
    ApiNewVersion VARCHAR(50),
    DifferentialTypeID INTEGER,
    DifferentialTimingID INTEGER,
    ElementPath VARCHAR(500),
    OldElement VARCHAR(500),
    NewElement VARCHAR(500), 
    ApiResource VARCHAR(500),
    ApiElementTypeID INTEGER,

    FOREIGN KEY (DifferentialTypeID)
        REFERENCES DifferentialType(DifferentialTypeID),
    FOREIGN KEY (DifferentialTimingID)
        REFERENCES DifferentialTiming(DifferentialTimingID),
    FOREIGN KEY (ApiElementTypeID)
        REFERENCES ApiElementType(ApiElementTypeID)
);


/**
*   Taxonomy
*/
DROP TABLE IF EXISTS Taxonomy;
CREATE TABLE Taxonomy (
    TaxonomyID INTEGER PRIMARY KEY,
    Description VARCHAR(500),
    DifferentialTypeID INTEGER,
    DifferentialTimingID INTEGER,
    ApiElementTypeID INTEGER,
    AdaptationNodeID INTEGER,

    FOREIGN KEY (DifferentialTypeID)
         REFERENCES DifferentialType(DifferentialTypeID),
    FOREIGN KEY (ApiElementTypeID)
         REFERENCES ApiElementType(ApiElementTypeID),
    FOREIGN KEY (AdaptationNodeID)
         REFERENCES AdaptationNode(AdaptationNodeID)
);


/**
*   AdaptationNode
*/
DROP TABLE IF EXISTS AdaptationNode;
CREATE TABLE AdaptationNode (
    AdaptationNodeID INTEGER PRIMARY KEY,
    TaxonomyID INTEGER,
    AdaptationNodeName VARCHAR(100),
    AdaptationNodeDescription VARCHAR(500),
    AdaptationNodeVerb VARCHAR(10),
    AdaptationNodePath VARCHAR(500),
    AdaptationNodeRequest VARCHAR(500),
    AdaptationNodeResponse VARCHAR(500),

    FOREIGN KEY (TaxonomyID) REFERENCES Taxonomy(TaxonomyID)
);


/**
*   DifferentialAdaptation
*/
DROP TABLE IF EXISTS DifferentialAdaptation;
CREATE TABLE DifferentialAdaptation (
    DifferentialAdaptationID INTEGER PRIMARY KEY,
    DifferentialID INTEGER,
    AdaptationNodeID INTEGER,
    ApiServer VARCHAR(500),
    ApiResource VARCHAR(500),
    AdaptationNodeVerb VARCHAR(10),
    AdaptationNodePath VARCHAR(500),
    AdaptationNodeRequest VARCHAR(500),
    AdaptationNodeResponse VARCHAR(500),
    DifferentialTypeID INTEGER,
    DifferentialTimingID INTEGER,
    ElementPath VARCHAR(500),
    OldElement VARCHAR(500),
    NewElement VARCHAR(500),
    ApiOldVersion VARCHAR(50),
    ApiNewVersion VARCHAR(50),

    FOREIGN KEY (DifferentialID) REFERENCES Differential(DifferentialID),
    FOREIGN KEY (AdaptationNodeID)
        REFERENCES AdaptationNode(AdaptationNodeID),
    FOREIGN KEY (DifferentialTypeID)
        REFERENCES DifferentialType(DifferentialTypeID),
    FOREIGN KEY (DifferentialTimingID)
        REFERENCES DifferentialTiming(DifferentialTimingID)
);

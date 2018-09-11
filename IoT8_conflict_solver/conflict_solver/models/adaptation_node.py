from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from models.model import db

##app = Flask(__name__)
#self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///conflict_solver.db'

#db = SQLAlchemy(app)

class AdaptationNode():
    def __init__(self, 
            AdaptationNodeID=0,
            TaxonomyID=0,
            AdaptationNodeName='',
            AdaptationNodeDescription='',
            AdaptationNodeVerb='',
            AdaptationNodePath='',
            AdaptationNodeRequest='',
            AdaptationNodeResponse=''):

        self.AdaptationNodeID=AdaptationNodeID,
        self.TaxonomyID=TaxonomyID,
        self.AdaptationNodeName=AdaptationNodeName,
        self.AdaptationNodeDescription=AdaptationNodeDescription,
        self.AdaptationNodeVerb=AdaptationNodeVerb,
        self.AdaptationNodePath=AdaptationNodePath,
        self.AdaptationNodeRequest=AdaptationNodeRequest,
        self.AdaptationNodeResponse=AdaptationNodeResponse

        if not self.AdaptationNodeID > 0:
            delattr(self, 'AdaptationNodeID')

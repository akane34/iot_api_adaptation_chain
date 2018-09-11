from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import text
from server import app

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class ApiElementType(db.Model):
    ApiElementTypeID = db.Column(db.Integer, primary_key=True)
    ApiElementTypeName = db.Column(db.String(500))
    ApiElementTypeDescription = db.Column(db.String(500))

    def save(self, ApiElementType):
        db.session.add(ApiElementType)
        db.session.commit()

    def findAll(self):
        return self.query.all()

class DifferentialType(db.Model):
    DifferentialTypeID = db.Column(db.Integer, primary_key=True)
    DifferentialTypeDescription = db.Column(db.String(500))

    def save(self, DifferentialType):
        db.session.add(DifferentialType)
        db.session.commit()

    def findAll(self):
        return self.query.all()

class DifferentialTiming(db.Model):
    DifferentialTimingID = db.Column(db.Integer, primary_key=True)
    DifferentialTimingName = db.Column(db.String(100))
    DifferentialTimingDescription = db.Column(db.String(500))

    def save(self, DifferentialTiming):
        db.session.add(DifferentialTiming)
        db.session.commit()

    def findAll(self):
        return self.query.all()

class Differential(db.Model):
    DifferentialID = db.Column(db.Integer, primary_key=True)
    ApiName = db.Column(db.String(500))
    ApiServer = db.Column(db.String(500))
    ApiOldVersion = db.Column(db.String(50))
    ApiNewVersion = db.Column(db.String(50))
    DifferentialTypeID = db.Column(db.Integer, db.ForeignKey('differential_type.DifferentialTypeID', use_alter=True), nullable=False)
    DifferentialTimingID = db.Column(db.Integer, db.ForeignKey('differential_timing.DifferentialTimingID'), nullable=False)
    ElementPath = db.Column(db.String(500))
    OldElement = db.Column(db.String(500))
    NewElement = db.Column(db.String(500))
    ApiResource = db.Column(db.String(500))
    ApiElementTypeID = db.Column(db.Integer, db.ForeignKey('api_element_type.ApiElementTypeID'), nullable=False)

    def save(self, Differential):
        db.session.add(Differential)
        db.session.commit()

    def findAll(self):
        return self.query.all()

class Taxonomy(db.Model):
    TaxonomyID = db.Column(db.Integer, primary_key=True)
    Description = db.Column(db.String(500))
    DifferentialTypeID = db.Column(db.Integer, db.ForeignKey('differential_type.DifferentialTypeID'), nullable=False)
    DifferentialTimingID = db.Column(db.Integer, db.ForeignKey('differential_timing.DifferentialTimingID'), nullable=False)
    ApiElementTypeID = db.Column(db.Integer, db.ForeignKey('api_element_type.ApiElementTypeID'), nullable=False)
    AdaptationNodeID = db.Column(db.Integer, db.ForeignKey('adaptation_node.AdaptationNodeID'))

    def save(self, Taxonomy):
        db.session.add(Taxonomy)
        db.session.commit()

    def findAll(self):
        resultproxy = db.engine.execute(text("select * from taxonomy"))
        d, a = {}, []
        for rowproxy in resultproxy:
            # rowproxy.items() returns an array like [(key0, value0), (key1, value1)]
            for tup in rowproxy.items():
                # build up the dictionary
                d = {**d, **{tup[0]: tup[1]}}
            a.append(d)

        return self.query.all()

class AdaptationNode(db.Model):
    AdaptationNodeID = db.Column(db.Integer, primary_key=True)
    TaxonomyID = db.Column(db.Integer, db.ForeignKey('taxonomy.TaxonomyID'))
    AdaptationNodeName = db.Column(db.String(100))
    AdaptationNodeDescription = db.Column(db.String(500))
    AdaptationNodeVerb = db.Column(db.String(10))
    AdaptationNodePath = db.Column(db.String(500))
    AdaptationNodeRequest = db.Column(db.String(500))
    AdaptationNodeResponse = db.Column(db.String(500))

    def Save(self, AdaptationNode):
        db.session.add(AdaptationNode)
        db.session.commit()

    def FindAll(self):
        return self.query.all()

class DifferentialAdaptation(db.Model):
    DifferentialAdaptationID = db.Column(db.Integer, primary_key=True)
    DifferentialID = db.Column(db.Integer, db.ForeignKey('differential.DifferentialID'))
    AdaptationNodeID = db.Column(db.Integer, db.ForeignKey('adaptation_node.AdaptationNodeID'))
    ApiServer = db.Column(db.String(500))
    ApiResource = db.Column(db.String(500))
    AdaptationNodeVerb = db.Column(db.String(10))
    AdaptationNodePath = db.Column(db.String(500))
    AdaptationNodeRequest = db.Column(db.String(500))
    AdaptationNodeResponse = db.Column(db.String(500))
    DifferentialTypeID = db.Column(db.Integer, db.ForeignKey('differential_type.DifferentialTypeID'))
    DifferentialTimingID = db.Column(db.Integer, db.ForeignKey('differential_timing.DifferentialTimingID'))
    ElementPath = db.Column(db.String(500))
    OldElement = db.Column(db.String(500))
    NewElement = db.Column(db.String(500))
    ApiOldVersion = db.Column(db.String(50))
    ApiNewVersion = db.Column(db.String(50))

    def save(self, DifferentialAdaptation):
        db.session.add(DifferentialAdaptation)
        db.session.commit()

    def findAll(self):
        return self.query.all()

    def executeInsert(self, sqlString):
        sql = text(sqlString)
        result = db.engine.execute(sql).execution_options(autocommit=True)
        return result
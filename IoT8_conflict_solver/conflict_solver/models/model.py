import sqlite3
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import text
from server import app

db = SQLAlchemy(app)
migrate = Migrate(app, db)

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

connection = sqlite3.connect('../conflict_solver.db')
connection.row_factory = dict_factory
dbcursor = connection.cursor()

class ApiElementType(db.Model):
    ApiElementTypeID = db.Column(db.Integer, primary_key=True)
    ApiElementTypeName = db.Column(db.String(500))
    ApiElementTypeDescription = db.Column(db.String(500))

    def save(self, ApiElementType):
        db.session.add(ApiElementType)
        db.session.commit()

    def findAll(self):
        dbcursor.execute('SELECT * FROM ApiElement')
        return dbcursor.fetchall()

class DifferentialType(db.Model):
    DifferentialTypeID = db.Column(db.Integer, primary_key=True)
    DifferentialTypeDescription = db.Column(db.String(500))

    def save(self, DifferentialType):
        db.session.add(DifferentialType)
        db.session.commit()

    def findAll(self):
        dbcursor.execute('SELECT * FROM DifferentialType')
        return dbcursor.fetchall()

class DifferentialTiming(db.Model):
    DifferentialTimingID = db.Column(db.Integer, primary_key=True)
    DifferentialTimingName = db.Column(db.String(100))
    DifferentialTimingDescription = db.Column(db.String(500))

    def save(self, DifferentialTiming):
        db.session.add(DifferentialTiming)
        db.session.commit()

    def findAll(self):
        dbcursor.execute('SELECT * FROM DifferentialTiming')
        return dbcursor.fetchall()

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

    def save(self, differentials):
        for diff in differentials:
            db.session.add(diff)
            db.session.commit()

    def findAll(self):
        dbcursor.execute('SELECT * FROM Differential')
        return dbcursor.fetchall()

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
        dbcursor.execute('SELECT * FROM Taxonomy')
        return dbcursor.fetchall()

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

    def findAll(self):
        dbcursor.execute('SELECT * FROM AdaptationNode')
        return dbcursor.fetchall()

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
        dbcursor.execute('SELECT * FROM DifferentialAdaptation')
        return dbcursor.fetchall()

    def executeInsert(self, sqlString):
        sql = text(sqlString)
        #result = db.engine.execute(sql).execution_options(autocommit=True)
        result = db.engine.execute(sql)

        return result
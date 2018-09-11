import sqlite3
import os

connection = str(os.getenv(key='CONFLICT_SOLVER_DATABASE'))

class DBManager():
    def selectAll(model, criteria=None):
        cursor = connection.cursor()
        cursor.execute("SELECT Site.lat, Site.long FROM Site;")
        results = cursor.fetchall()
        for r in results:
            print(r)
        cursor.close()
        connection.close()

        return db.selectAll(model, criteria)

    def selectOne(model, criteria):
        db = DBManager().getDatabase()
        return db.selectOne(model, criteria)


from pymongo import MongoClient
from bson import ObjectId

class AggregationsService(object):
    def __init__(self,
                 db_host = str,
                 db_name: str = 'exampleDB', 
                 #db_collections: list[str] = ['exampleCollection'],
                 ) -> None:
        self.db_host = db_host
        self.db_name = db_name
        #self.db_collections = db_collections
        self.service = MongoClient(db_host)
        self.data_base = self.service[db_name]

    def setDBHost(self, db_host):
        self.db_host = db_host

    def setDBName(self, db_name):
        self.db_name = db_name

    def setDBCollections(self, db_collections):
        self.db_collections = db_collections

    def restartService(self, db_host, db_name):
        self.service = MongoClient(db_host)
        self.data_base = self.service[db_name]

    def getAllEmbeddedObjects(self, collection_name: str, obj_id: str):
        obj_id = ObjectId(obj_id)
        jsonObj = self.data_base[collection_name].find_one(obj_id)
        
        self.data_base[collection_name].aggregate([
            {
                "$lookup": {
                    "from": collection_name,
                    "localField": "_id",
                    "foreignField": "_id",
                    "as": collection_name
                },
                "$match": {
                    "_id": obj_id
                },
                "$project": {
                    "_id": 0,
                    collection_name: 1
                }
            }
        ])

    def getHabilidadesForUser(self, collection_name: str, user_id: str):
        self.data_base[collection_name].aggregate(
            [
                {
                    '$match': {
                        '_id': ObjectId(user_id)
                    }
                }, {
                    '$unwind': {
                        'path': '$habilidades', 
                        'preserveNullAndEmptyArrays': True
                    }
                }, {
                    '$unwind': {
                        'path': '$equipo.armas', 
                        'preserveNullAndEmptyArrays': True
                    }
                }, {
                    '$unwind': {
                        'path': '$equipo.armas.habilidad', 
                        'preserveNullAndEmptyArrays': True
                    }
                }, {
                    '$unwind': {
                        'path': '$equipo.equipamiento', 
                        'preserveNullAndEmptyArrays': True
                    }
                }, {
                    '$unwind': {
                        'path': '$equipo.equipamiento.habilidad', 
                        'preserveNullAndEmptyArrays': True
                    }
                }, {
                    '$group': {
                        '_id': None, 
                        'habilidades_totales': {
                            '$addToSet': '$habilidades'
                        }, 
                        'habilidades_armas': {
                            '$addToSet': '$equipo.armas.habilidad'
                        }, 
                        'habilidad_equipo': {
                            '$addToSet': '$equipo.equipamiento.habilidad'
                        }
                    }
                }, {
                    '$project': {
                        '_id': 0, 
                        'habilidades_totales': {
                            '$concatArrays': [
                                '$habilidades_totales', '$habilidades_armas', '$habilidad_equipo'
                            ]
                        }
                    }
                }
            ]
        )

if __name__ == "__main__":
    service = AggregationsService("mongodb+srv://Cluster18604:mati2002@cluster0.zale6eu.mongodb.net/", "MMO_RPG1")
    service.getAllEmbeddedObjects("Personaje", "652ed7e8fa9783ea7729bd81")
from pymongo import MongoClient
from bson import ObjectId

class QueriesService(object):
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

    def getJugadoresPorNivel(self, min_level: int=0, max_level: int|None=None):
        if max_level is None:
            max_level = min_level
        resultado = self.data_base.Personaje.find(
            {
                'nivel': {
                    '$gt': min_level, 
                    '$lt': max_level
                }
            }
        )
        return resultado
    
    def getJuegadoresPorNombre(self):
        query = [{  
            "$project": {
            "_id": 0, 
            "nombre": "$nombre" 
            }}
        ]
        return self.db_name.Personaje.aggregate(query)

    def getHabilidadesporUserID(self, user_id):
        query=[
                {
                    '$match': {
                        '_id': ObjectId(user_id)
                    }
                }, {
                    '$project': {
                        'habilidades': 1, 
                        'equipo.armas.habilidad': 1, 
                        'equipo.equipamiento.habilidad': 1
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
                            '$addToSet': '$habilidades',
                            '$addToSet': '$equipo.armas.habilidad',
                            '$addToSet': '$equipo.equipamiento.habilidad'
                        }
                    }
                }, {
                    '$project': {
                        '_id': 0, 
                        'habilidades_totales': 1
                    }
                }
            ]   
    
    def getHabilidadesPorUserNombre(self, user_id):
        query=[
            {
                '$match': {
                    '_id': ObjectId('652f2ef059a914737585627d')
                }
            }, {
                '$unwind': '$habilidades'
            }, {
                '$lookup': {
                    'from': 'Habilidad', 
                    'localField': 'habilidades._id', 
                    'foreignField': '_id', 
                    'as': 'habilidades_info'
                }
            }, {
                '$project': {
                    '_id': 0, 
                    'nombre_habilidad': '$habilidades_info.nombre'
                }
            }, {
                '$unwind': '$nombre_habilidad'
            }
        ]
        return self.db_name.Personaje.aggregate(query)
        
    def getPersonajePorMision(self, mission_id):
        pass
        
    def getObjetosPorValor(self, min_val: int=0, max_val: int|None=None):
        if max_val is None:
            max_val = min_val
        resultado = self.data_base.Objeto_Clave.find(
           {
            'valor': {
            '$gt': min_val, 
            '$lt': max_val
                    }
            } 
        )
        return resultado
    
    def getAllEmbeddedObjects(self):
            [
                {
                    $match: {
                    _id: ObjectId("652f2ef059a914737585627f"),
                    },
                },
                {
                    $lookup: {
                    from: "Habilidad",
                    localField: "habilidades._id",
                    foreignField: "_id",
                    as: "habilidades",
                    },
                },
                {
                    $lookup: {
                    from: "Mision",
                    localField: "misiones._id",
                    foreignField: "_id",
                    as: "misiones",
                    },
                },
            ]        

    
    
if __name__ == "__main__":
    service = QueriesService("mongodb+srv://Cluster18604:mati2002@cluster0.zale6eu.mongodb.net/", "MMO_RPG1")
    print(service.getHabilidadesPorUser('652f2ef059a914737585627d'))
    print(service.getJugadoresPorNivel(20))

    
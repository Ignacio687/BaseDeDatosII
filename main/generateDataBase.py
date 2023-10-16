from pymongo import MongoClient
from main import  SkillsGenerator, ConsumiblesGenerator, KeyObjectsGenerator, MisionesGenerator

class DataBaseGenerator():
    def __init__(self,
                 db_host = str,
                 db_name: str = 'exampleDB', 
                 db_collections: list[str] = ['exampleCollection']
                 ) -> None:
        self.db_host = db_host
        self.db_name = db_name
        self.db_collections = db_collections

    def setDBHost(self, db_host):
        self.db_host = db_host

    def setDBName(self, db_name):
        self.db_name = db_name

    def setDBCollections(self, db_collections):
        self.db_collections = db_collections

    def generateJsonData(self, collectionName:str, data_base):
        generators = {}
        generatorsList = [("habilidad", SkillsGenerator), ("consumible", ConsumiblesGenerator), ("objeto_clave", KeyObjectsGenerator), ("mision", MisionesGenerator)]
        for name, classVar in generatorsList:
            instance = classVar()
            generators[name] = instance
        try:
            return generators[collectionName.lower()].generateData(collectionName, data_base)
        except KeyError:
            return [{"ERROR": "No existe un generador para esta coleccion"}]

    def generateDB(self):
        cliente = MongoClient(self.db_host)
        cliente.drop_database(self.db_name)
        db = cliente[self.db_name]
        for collection in self.db_collections:
            db[collection].insert_many(self.generateJsonData(collection, db))
        cliente.close()
        print("Proceso Finalizado")
        
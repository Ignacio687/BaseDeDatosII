import pymongo, json
from pymongo import MongoClient
from bson import ObjectId
from main import  SkillsGenerator

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

    def generateJsonData(self, collectionName:str):
        if collectionName.lower() == 'habilidad':
            skillsGenerator = SkillsGenerator()
            return skillsGenerator.generateData(collectionName)
        else: return [{}]

    def generateDB(self):
        cliente = MongoClient(self.db_host)
        cliente.drop_database(self.db_name)
        db = cliente[self.db_name]
        for collection in self.db_collections:
            db[collection].insert_many(self.generateJsonData(collection))
        cliente.close()
        print("Proceso Finalizado")
        

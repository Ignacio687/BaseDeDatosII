from pymongo import MongoClient
from main import  SkillsGenerator, ConsumiblesGenerator, KeyObjectsGenerator, MisionesGenerator, GeneratorPersonaje
import datetime

class DataBaseGenerator():
    def __init__(self,
                 db_host = str,
                 db_name: str = 'exampleDB', 
                 db_collections: list[str] = ['exampleCollection'],
                 cantPersonajes: int = 0,
                 ) -> None:
        self.db_host = db_host
        self.db_name = db_name
        self.db_collections = db_collections
        self.deleteDBFlag = False
        self.cantPersonajes = cantPersonajes
        self.deleteColectionFlag = False

    def setcantPersonajes(self, cantPersonajes):
        self.cantPersonajes = cantPersonajes

    def setDeleteColectionFlag(self, conditional: bool=False):
        self.deleteColectionFlag = conditional

    def setDeleteDBFlag(self, conditional: bool=False):
        self.deleteDBFlag = conditional

    def setDBHost(self, db_host):
        self.db_host = db_host

    def setDBName(self, db_name):
        self.db_name = db_name

    def setDBCollections(self, db_collections):
        self.db_collections = db_collections

    def generateJsonData(self, collectionName:str, data_base):
        generators = {}
        generatorsList = [("habilidad", SkillsGenerator), ("consumible", ConsumiblesGenerator), ("objeto_clave", KeyObjectsGenerator), ("mision", MisionesGenerator), ("personaje", GeneratorPersonaje)]
        for name, classVar in generatorsList:
            instance = classVar()
            generators[name] = instance
        try:
            if collectionName.lower() == "personaje":
                return generators[collectionName.lower()].generateData(collectionName, data_base, self.cantPersonajes)
            return generators[collectionName.lower()].generateData(collectionName, data_base)
        except KeyError as e:
            return [{"ERROR": "No existe un generador para esta coleccion"}]

    def generateDB(self):
        cliente = MongoClient(self.db_host)
        if self.deleteDBFlag:
            print('Borrando DB')
            cliente.drop_database(self.db_name)
            print('DB Borrada')
            db = cliente[self.db_name]
        elif self.deleteColectionFlag:
            db = cliente[self.db_name]
            for collection in self.db_collections:
                print(f"Borrando coleccion {collection}")
                db[collection].drop()
        else:
             db = cliente[self.db_name]
        for collection in self.db_collections:
            print(f"Generando colección {collection}")
            files = self.generateJsonData(collection, db)
            db[collection].insert_many(files)
        cliente.close()
        print("Proceso Finalizado")
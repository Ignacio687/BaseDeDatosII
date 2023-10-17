from pymongo import MongoClient
from main import  SkillsGenerator, ConsumiblesGenerator, KeyObjectsGenerator, MisionesGenerator, GeneratorPersonaje
import multiprocessing

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

    def setcantPersonajes(self, cantPersonajes):
        self.cantPersonajes = cantPersonajes

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
                # pool = multiprocessing.Pool()
                # totalTimeList = pool.imap_unordered(self.uploadPersonajeData, generators['personaje'].generateData(collectionName, data_base, self.cantPersonajes))
                # totalTime = 0
                # for time in totalTimeList:
                #     totalTime += time
                # print(f"Tiempo promedio de creacion de usuario:  {round(totalTime/self.cantPersonajes, 2)} s")
                # print(f"Tiempo total: {totalTime}")
                # pool.close()
                # pool.join()
                return generators['personaje'].generateData(collectionName, data_base, self.cantPersonajes)
            else:
                return generators[collectionName.lower()].generateData(collectionName, data_base)
        except KeyError:
            return [{"ERROR": "No existe un generador para esta coleccion"}]

    def generateDB(self):
        cliente = MongoClient(self.db_host)
        if self.deleteDBFlag:
            print('Borrando DB')
            cliente.drop_database(self.db_name)
            print('DB Borrada')
        db = cliente[self.db_name]
        for collection in self.db_collections:
            if collection == 'Personaje':
                print(f"Generando colección {collection}")
                totalTime = 0
                for personajeObj in self.generateJsonData(collection, db):
                    totalTime += personajeObj[1]
                print(f"Tiempo promedio de creacion de usuario:  {round(totalTime/self.cantPersonajes, 2)} s")
                print(f"Tiempo total: {totalTime}")
            else:
                print(f"Generando colección {collection}")
                db[collection].insert_many(self.generateJsonData(collection, db))
        cliente.close()
        print("Proceso Finalizado")
        
    def uploadPersonajeData(self, jsonObj):
        #db.Personaje.insert_one(jsonObj[0])
        return jsonObj[1]
from main.generateDataBase import DataBaseGenerator

if __name__ == "__main__":
    db = DataBaseGenerator("mongodb+srv://Cluster18604:mati2002@cluster0.zale6eu.mongodb.net/")
    db.setDBCollections(['Habilidad', 'Consumible', 'Objeto_Clave', 'Mision', 'Enemigos'])
    db.setDBName("MMO_RPG1")
    db.generateDB()
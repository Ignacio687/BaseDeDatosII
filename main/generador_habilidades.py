import pymongo
from pymongo import MongoClient
import random,json

nombres = ["Espada del Destino", "Arco de la Luna", "Varita de Fuego", "Hacha del Guerrero", "Baston del Sabio"]
tipos_arma = ["Arma cuerpo a cuerpo", "Arma de fuego", "Arco y flecha", "Varita magica"]
requerimientos = ["Cazador", "Mago", "Guerrero", "Asesino", "Sanador"]


cliente = pymongo.MongoClient("mongodb+srv://Cluster18604:mati2002@cluster0.zale6eu.mongodb.net/")
db = cliente.MMO_RPG  # Reemplaza "tu_base_de_datos" con el nombre de tu base de datos
coleccion = db.Habilidades  # Reemplaza "tu_coleccion" con el nombre de tu colección

def generar_registro():
    return {
        "nombre": random.choice(nombres),
        "dano-min": random.randint(5, 10),
        "dano-max": random.randint(15, 25),
        "puntos_de_accion": random.randint(1, 5),
        "alcance": round(random.uniform(1, 10), 2),
        "recarga": round(random.uniform(0.5, 2), 2),
        "efectos": [{"info": "El dano se basa en tu ataque basico y ora recibe una bonificacion de Fuerza."}],
        "requerimiento": [
            {"tipo": random.choice(tipos_arma)},
            {random.choice(requerimientos): random.randint(1, 5)}
        ]
    }

registros = [generar_registro() for _ in range(10)]
registros_json = json.dumps(registros, indent=4)

with open('data/habilidades.json', 'w') as archivo_json:
    archivo_json.write(registros_json)

if input("Confirmar?") == 'y':
    coleccion.insert_many(registros)
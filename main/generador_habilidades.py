import pymongo
from pymongo import MongoClient
import random,json

nombres = {
    "Cazador": "Obten mas carne y piel de animales que cazes.",
    "Medico": "Curas a otros mas eficientemente y te curas a ti mismo mas rapidamente.",
    "Atleta": "Corres mas rapido y gastas menos resistencia al correr.",
    "Montañero": "Escalas mas rapido y consumes menos resistencia al escalar.",
    "Nutricionista": "Obten mas beneficios al comer y beber.",
    "Bien Nutrido": "Aumenta la duracion de los beneficios de la comida y bebida que consumes.",
    "Busqueda Rapida": "Buscas mas rapido en los contenedores y recipientes.",
    "Negociante": "Consigues mejores precios al comprar y vender en las tiendas de los comerciantes.",
    "Ingeniero": "Desbloquea la capacidad de crear objetos avanzados.",
    "Piromano": "Haz mas daño con armas y trampas que infligen fuego.",
    "Minero": "Obten mas recursos al extraer minerales y rocas.",
    "Trabajo en Equipo": "Obten mas experiencia cuando estas en un grupo con otros jugadores.",
    "Fuerza de Voluntad": "Recibes menos penalizaciones por tener hambre o sed.",
    "Sexo Tecnico": "Recibes menos penalizaciones por morir y pierdes menos experiencia al morir.",
    "Constructor": "Gastas menos recursos al construir y reparar objetos.",
    "Agricultor": "Cultivas plantas mas rapido y obtienes mas recursos de las cosechas.",
    "Reciclaje": "Obten mas materiales al desmontar objetos.",
    "Rapido y Furioso": "Haz mas daño con armas cuerpo a cuerpo.",
    "Resistente a las Enfermedades": "Tienes menos probabilidad de contraer enfermedades.",
    "Maestro de las Sombras": "Te vuelves invisible en la oscuridad.",
    "Control Mental": "Puedes persuadir a otros personajes y criaturas para que hagan lo que quieras.",
    "Teletransporte": "Puedes teletransportarte a lugares que has visitado previamente.",
    "Vision Nocturna": "Puedes ver claramente en la oscuridad.",
    "Inteligencia Artificial": "Aumenta tu inteligencia artificial, permitiendote aprender y adaptarte mas rapido.",
    "Manipulador del Tiempo": "Puedes ralentizar o acelerar el tiempo a tu alrededor.",
    "Control de Elementos": "Puedes controlar el fuego, agua, tierra y aire a tu voluntad.",
    "Vuelo": "Puedes volar en el aire como un pajaro o un superheroe.",
    "Sanador": "Puedes curar las heridas de otros y mejorar su salud.",
    "Control de Bestias": "Puedes comunicarte y controlar animales y bestias.",
    "Inmortalidad": "Eres inmune a la muerte y al envejecimiento.",
    "Control de Energia": "Puedes manipular y utilizar diversas formas de energia.",
    "Telepatia": "Puedes leer mentes y comunicarte telepaticamente con otros.",
    "Maestro de Disfraz": "Puedes cambiar tu apariencia y adoptar la forma de cualquier persona u objeto.",
    "Absorcion de Daño": "Puedes absorber y reflejar el daño que otros te infligen."
}
tipos_req_habilidades =["Aeroteurgo","Canalla","Cazador","Contienda","Geomante","Hidrosofista","Invocacion","Necromante","Piroquinetico","Polimorfismo",]
tipos_req_arma = ["A distancia","A dos manos","A una mano","Empuñar dos armas"]


cliente = pymongo.MongoClient("mongodb+srv://Cluster18604:mati2002@cluster0.zale6eu.mongodb.net/")
db = cliente.MMO_RPG  # Reemplaza "tu_base_de_datos" con el nombre de tu base de datos
coleccion = db.Habilidades  # Reemplaza "tu_coleccion" con el nombre de tu coleccion

def generar_registro(key,element):
    return {
        "nombre": key,
        "dano-min": random.randint(5, 10),
        "dano-max": random.randint(15, 25),
        "puntos_de_accion": random.randint(1, 5),
        "alcance": round(random.uniform(1, 10), 2),
        "recarga": round(random.uniform(0.5, 2), 2),
        "efectos": [{"info": element}],
        "requerimiento": [
            {"tipo": random.choice(tipos_req_habilidades)},
            {random.choice(tipos_req_arma): random.randint(1, 5)}
        ]
    }

registros = [generar_registro(key,element) for key,element in nombres.items()]
registros_json = json.dumps(registros, indent=4)

with open('data/habilidades.json', 'w') as archivo_json:
    archivo_json.write(registros_json)

if input("Confirmar?") == 'y':
    coleccion.insert_many(registros)
import random
from . import GeneratorABC
from typing import Any

class SkillsGenerator(GeneratorABC):
    def __init__(self) -> None:
        self.nombres = {
            "Cazador": "Obten mas carne y piel de animales que cazes.",
            "Medico": "Curas a otros mas eficientemente y te curas a ti mismo mas rapidamente.",
            "Atleta": "Corres mas rapido y gastas menos resistencia al correr.",
            "Montanero": "Escalas mas rapido y consumes menos resistencia al escalar.",
            "Nutricionista": "Obten mas beneficios al comer y beber.",
            "Bien Nutrido": "Aumenta la duracion de los beneficios de la comida y bebida que consumes.",
            "Busqueda Rapida": "Buscas mas rapido en los contenedores y recipientes.",
            "Negociante": "Consigues mejores precios al comprar y vender en las tiendas de los comerciantes.",
            "Ingeniero": "Desbloquea la capacidad de crear objetos avanzados.",
            "Piromano": "Haz mas dano con armas y trampas que infligen fuego.",
            "Minero": "Obten mas recursos al extraer minerales y rocas.",
            "Trabajo en Equipo": "Obten mas experiencia cuando estas en un grupo con otros jugadores.",
            "Fuerza de Voluntad": "Recibes menos penalizaciones por tener hambre o sed.",
            "Sexo Tecnico": "Recibes menos penalizaciones por morir y pierdes menos experiencia al morir.",
            "Constructor": "Gastas menos recursos al construir y reparar objetos.",
            "Agricultor": "Cultivas plantas mas rapido y obtienes mas recursos de las cosechas.",
            "Reciclaje": "Obten mas materiales al desmontar objetos.",
            "Rapido y Furioso": "Haz mas dano con armas cuerpo a cuerpo.",
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
            "Absorcion de Dano": "Puedes absorber y reflejar el dano que otros te infligen."
        }
        self.bonificaciones = [
            "El dano se basa en tu ataque basico y recibe una bonificacion de Fuerza.",
            "Incrementa tu velocidad de movimiento en un 10% al equipar botas magicas.",
            "Ganas un 5% de resistencia a los ataques magicos gracias a tu amuleto encantado.",
            "Los golpes criticos causan el doble de dano.",
            "Tus hechizos de fuego queman a los enemigos durante 3 segundos.",
            "El veneno infligido a los enemigos drena su vida durante el tiempo.",
            "La armadura pesada reduce el dano recibido de los ataques fisicos en un 20%.",
            "Las dagas gemelas otorgan un 15% de probabilidad de esquivar los ataques enemigos.",
            "Recibes un 10% mas de oro al derrotar monstruos.",
            "Los ataques cuerpo a cuerpo infligen un 5% de dano adicional.",
            "Las flechas envenenadas causan dano a lo largo del tiempo.",
            "Tu escudo magico te protege de los hechizos de hielo.",
            "Los craneos malditos reducen la resistencia magica de los enemigos en un 15%.",
            "Tu armadura de placas refleja el 25% del dano recibido de vuelta al atacante.",
            "Los pergaminos de teleportacion te permiten moverte instantaneamente a ciudades conocidas.",
            "La regeneracion de salud aumenta en un 2% por cada punto de inteligencia.",
            "El anillo de invisibilidad te hace invisible a los enemigos mientras estas quieto.",
            "Las pociones de resistencia mejoran temporalmente tus defensas.",
            "Los ataques criticos infligen un estado de aturdimiento en los enemigos.",
            "El libro de hechizos aumenta el poder magico en un 10%.",
            "Los tatuajes runicos mejoran tus habilidades magicas.",
            "Los guerreros berserker ganan un 20% de dano adicional cuando estan heridos.",
            "Las botas aladas te permiten saltar distancias largas.",
            "Las joyas magicas aumentan tu mana maximo en un 15%.",
            "Las espadas runicas son efectivas contra criaturas demoniacas.",
            "Las joyas de la suerte aumentan las probabilidades de encontrar tesoros.",
            "El anillo de la vida te otorga resistencia a la muerte una vez al dia.",
            "Los elixires de velocidad aumentan temporalmente tu velocidad de ataque.",
            "El casco de los sabios mejora tus habilidades de adivinacion.",
            "Los guantes del ladron aumentan tus habilidades de sigilo.",
            "Las ballestas magicas disparan flechas magicas a los enemigos.",
            "Las varitas de curacion restauran tu salud gradualmente.",
            "El escudo de la justicia protege contra los ataques malditos.",
            "Las armas de luz infligen dano adicional a los no muertos.",
            "Las armaduras encantadas te hacen inmune a los efectos de paralisis.",
            "Los talismanes sagrados repelen a los espiritus malignos.",
            "Las capas de sombra te vuelven invisible en la oscuridad.",
            "Los orbes de control permiten dominar a las bestias salvajes.",
            "Las dagas arrojadizas infligen dano critico a los enemigos desprevenidos."
        ]
        self.tipos_req_habilidades = ["Aeroteurgo","Canalla","Cazador","Contienda","Geomante","Hidrosofista","Invocacion","Necromante","Piroquinetico","Polimorfismo",]
        self.tipos_req_arma = ["A distancia","A dos manos","A una mano", "Arma Cuerpo a Cuerpo", "Arma Magica"]


    def generateJsonObj(self, key:str, element: Any) -> dict[str, Any]:
        return {
            "nombre": key,
            "dano-min": random.randint(5, 10),
            "dano-max": random.randint(15, 25),
            "puntos_de_accion": random.randint(1, 5),
            "alcance": random.randint(1, 5),
            "recarga": random.randint(1, 5),
            "detalle": element,
            "efecto": random.choice(self.bonificaciones),
            "requerimiento": [
                {"tipo": random.choice(self.tipos_req_arma)},
                {random.choice(self.tipos_req_habilidades): random.randint(1, 11)}
            ]
        }

    def generateData(self, name:str, data_base) -> list[dict[str, Any]]:
        registros = [self.generateJsonObj(key, element) for key,element in self.nombres.items()]
        self.generateJsonFile(registros, name)
        return registros
import random
from typing import Any
from . import GeneratorABC
from pymongo import MongoClient

class KeyObjectsGenerator(GeneratorABC):
    def __init__(self) -> None:
        self.objetos_clave = {
            "Llave del Templo Antiguo": "Una antigua llave de bronce que desbloquea la entrada al Templo Antiguo, repleto de tesoros perdidos.",
            "Talisman del Destino": "Un talisman magico que otorga a su portador la capacidad de cambiar su destino una vez.",
            "Perla de la Sabiduria": "Una hermosa perla que concede conocimiento y sabiduria a aquel que la posee.",
            "Espada de los Caidos": "Una espada legendaria que fue usada por heroes caidos en batalla. Infunde miedo en los enemigos.",
            "Espejo de la Verdad": "Un espejo magico que revela la verdad oculta y los enganos de aquellos que se reflejan en el.",
            "Gema del Fuego Eterno": "Una gema ardiente que puede encender fuego eterno y controlarlo a voluntad.",
            "Daga de las Sombras": "Una daga sigilosa que permite al portador desvanecerse en las sombras y atacar sin ser visto.",
            "Cetro de la Reina de Hielo": "El cetro de la legendaria Reina de Hielo, capaz de congelar a sus enemigos con un solo toque.",
            "Amuleto del Tiempo": "Un amuleto que concede al portador el control sobre el tiempo, permitiendole retroceder o avanzar en el tiempo.",
            "Flor de la Eterna Primavera": "Una hermosa flor que florece en todas las estaciones y otorga vida eterna a su dueno.",
            "Llave del Portal Interdimensional": "Una llave que puede abrir portales a dimensiones desconocidas y peligrosas.",
            "Orbe de la Luna Celestial": "Un orbe que canaliza el poder de la luna para otorgar habilidades magicas a su portador.",
            "Colmillo del Dragon": "Un colmillo afilado de un dragon antiguo que puede ser forjado en una espada legendaria.",
            "Libro de Hechizos Antiguos": "Un antiguo libro lleno de hechizos olvidados que otorga conocimientos arcanos.",
            "Bolsa de Monedas sin Fondo": "Una bolsa que siempre contiene monedas de oro, sin importar cuantas saques de ella.",
            "Martillo de los Dioses": "Un martillo imbuido con el poder de los dioses, capaz de desatar la furia divina en la batalla.",
            "Ojo del Oraculo": "Un ojo magico que permite al portador ver el futuro y obtener visiones de eventos por venir.",
            "Anillo del Inmortal": "Un anillo que concede la inmortalidad a su portador, volviendolo inmune al paso del tiempo.",
            "Calavera del Conquistador": "Una calavera tallada con runas que otorga el conocimiento de las estrategias de los conquistadores.",
            "Llave del Abismo Oscuro": "Una llave que abre la puerta al Abismo Oscuro, un lugar lleno de peligros y tesoros inimaginables.",
            "Corona del Rey Dragon": "Una corona adornada con gemas que simboliza el dominio sobre los dragones y sus poderes.",
            "Lanza del Cazador de Dragones": "Una lanza magica forjada para cazar dragones y perforar sus escamas con facilidad.",
            "Reloj de la Eternidad": "Un reloj que detiene el tiempo a voluntad y permite al portador moverse libremente en un mundo congelado.",
            "Hoja de la Luna Plateada": "Una espada de plata que brilla con la luz de la luna y es efectiva contra criaturas de la noche.",
            "Piedra del Portal Interplanar": "Una piedra que puede abrir portales a otros planos de existencia y conectar mundos diferentes.",
            "Llave del Tesoro del Pirata": "Una llave que desbloquea el legendario tesoro escondido por un famoso pirata.",
            "Pergamino del Sabio Anciano": "Un antiguo pergamino que contiene secretos perdidos y hechizos ancestrales.",
            "Corazon de la Selva Eterna": "Una gema que alberga el espiritu de la selva y otorga control sobre la naturaleza.",
            "Baston del Archimago": "Un baston que concentra el poder de un archimago y amplifica los hechizos del portador.",
            "Ojo del Huracan": "Un ojo que permite al portador controlar el viento y desatar tormentas furiosas.",
            "Gafas de la Vision Verdadera": "Un par de gafas magicas que revelan la verdad y las ilusiones ocultas.",
            "Cetro del Faraon": "Un cetro imbuido con la autoridad del faraon, que permite controlar a las criaturas no muertas.",
            "Cristal de los Suenos": "Un cristal que permite al portador entrar en los suenos de otros y explorar mundos oniricos.",
            "Flauta del Chaman": "Una flauta magica que puede comunicarse con espiritus y bestias de la naturaleza.",
            "Llave del Portal Estelar": "Una llave que abre puertas a mundos distantes y desconocidos en las estrellas.",
            "Amuleto de la Lluvia de Estrellas": "Un amuleto que otorga el poder de convocar lluvias de estrellas y desear deseos.",
            "Lanza de la Aurora": "Una lanza que irradia la luz de la aurora y puede purificar a las criaturas corruptas.",
            "Piedra de la Sabiduria Antigua": "Una piedra que contiene la sabiduria de civilizaciones antiguas y otorga conocimiento.",
            "Cetro de los Elementos": "Un cetro que permite al portador controlar los cuatro elementos: fuego, agua, tierra y aire.",
            "Espejo de la Dualidad": "Un espejo que crea una copia exacta del portador para luchar a su lado en batalla."
        }

    def generateJsonObj(self, key:str, element: Any) -> dict[str, Any]:
        return {
        "nombre": key,
        "descripcion": element,
        "peso": round(random.uniform(0.01, 2), 2) ,
        "valor": random.randint(10, 1000) 
        }

    def generateData(self, name:str, data_base) -> list[dict[str, Any]]:
        registros = [self.generateJsonObj(key, element) for key,element in self.objetos_clave.items()]
        self.generateJsonFile(registros, name)
        return registros

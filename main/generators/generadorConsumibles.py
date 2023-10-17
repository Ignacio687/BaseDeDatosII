import random
from . import GeneratorABC
from typing import Any
from itertools import product
from pymongo import MongoClient

class ConsumiblesGenerator(GeneratorABC):
    def __init__(self) -> None:
        self.tipos_objetos = ["pocion", "pan", "bomba molotov", "elixir", "piedra preciosa", "pergamino", "pocion de invisibilidad", "pocion de fuerza", "pocion de velocidad", "pocion de resistencia", "pocion de salud", "pocion de mana", "pocion de veneno", "pocion de fuego", "pocion de hielo", "pocion de electricidad", "pocion de curacion", "pocion de regeneracion"]
        self.adjetivos = ["poderoso", "magico", "encantado", "antiguo", "legendario", "oscuro", "resplandeciente", "divino", "caotico", "misterioso", "raro", "comun", "incomun", "epico", "unico", "maldito"]

    def generateJsonObj(self, key:str, element: Any) -> dict[str, Any]:
        atributos = ["Agilidad", "Inteligencia", "Resistencia", "Suerte", "Carisma", "Sabiduria", "Destreza", "Constitucion", "Percepcion", "Voluntad"]
        peso = round(random.uniform(0.01, 2), 2) 
        valor = random.randint(10, 100) 
        descripcion = f"Este/a {key} {random.choice([ 'tiene propiedades magicas', 'viene de un reino muy lejano', 'pertenece a una dinastia perdida', 'lo encontaste en el suelo', 'se uso en la guerra contra los elfos', 'fue conseguido tras derramar mucha sangre', 'se lo saco dios de dios sabe donde', 'parece bastante normal'])} y es {random.choice(['muy poderoso', 'antiguo, de una era olvidada', 'misterioso', 'un invento de la iglesia catolica', 'un objeto maldido', 'esencial para la supervicenai de los 7 reinos', 'mortal, en las manos adecuadas'])}."
        efectos = []
        for index in range(1, random.randint(2,6)):
            efecto = random.choice(atributos)
            if efecto not in [list(efecto.keys())[0] for efecto in efectos]:
                efectos.append({efecto: random.randint(1, 15)})
        duracion = random.randint(1, 10)

        return {
            "tipo": key,
            "nombre": f'{element} {key}',
            "peso": peso,
            "valor": valor,
            "descripcion": descripcion,
            "efectos": efectos,
            "duracion": duracion
        }

    def generateData(self, name:str, data_base) -> list[dict[str, Any]]:
        registros = [self.generateJsonObj(key, element) for key,element in product(self.tipos_objetos, self.adjetivos)]
        #self.generateJsonFile(registros, name)
        return registros
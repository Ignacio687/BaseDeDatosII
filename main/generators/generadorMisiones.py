import random, json
from bson import ObjectId
from typing import Any
from . import GeneratorABC, EquipmentGenerator

class MisionesGenerator(GeneratorABC):
    def __init__(self) -> None:
        self.nombres_de_misiones = [
    "La busqueda del artefacto perdido",
    "La maldicion de la cripta ancestral",
    "El secreto de la esmeralda dragon",
    "La venganza del lobo solitario",
    "La invasion de los orcos feroces",
    "El rescate de la princesa cautiva",
    "La busqueda del Libro de las Sombras",
    "El enigma de la estatua llameante",
    "La conspiracion en la corte real",
    "El robo del diamante del desierto",
    "La venganza del caballero caido",
    "La persecucion del ladron maestro",
    "La maldicion del bosque oscuro",
    "La leyenda de la espada legendaria",
    "La incursion en el templo prohibido",
    "El enigma de la piedra lunar",
    "La defensa del reino enano",
    "La traicion en la hermandad de los magos",
    "La amenaza de los no-muertos",
    "La reliquia de los antiguos",
    "El dilema de las dos lunas",
    "El rescate de la aldea perdida",
    "El misterio del barco fantasma",
    "La busqueda del corazon de la selva",
    "La venganza del corsario",
    "La profecia de los dioses antiguos",
    "El enigma de la estrella fugaz",
    "La venganza del pirata legendario",
    "La conspiracion de los asesinos",
    "La busqueda del tesoro maldito",
    "La maldicion del faro embrujado",
    "La amenaza del dragon de hielo",
    "La defensa de la torre de cristal",
    "El desafio de los elementos",
    "La traicion en la hermandad oscura",
    "La incursion en la fortaleza perdida",
    "El enigma de la ciudad olvidada",
    "El robo del colgante real",
    "La amenaza de los seres subterraneos",
    "La venganza del caballero renegado",
    "El misterio de la estatua ancestral",
    "La busqueda del libro de hechizos",
    "La maldicion de la mansion embrujada",
    "La conspiracion en la corte de las sombras",
    "La traicion en el gremio de ladrones",
    "La defensa de la aldea elfica",
    "El rescate de los prisioneros de guerra",
    "La venganza de la bruja malvada",
    "La persecucion del artefacto antiguo",
    "El enigma de la gema perdida",
]

        self.etapas_de_mision = [
    {
        "nombre": "Descubre indicios de la conspiracion.",
        "descripcion": "Indicios apuntan a una conspiracion en la corte real. Investiguemos para revelar la verdad detras de estos oscuros planes."
    },
    {
        "nombre": "Rastrea las pistas del ladron maestro.",
        "descripcion": "Un ladron maestro ha robado tesoros invaluables. Rastreemoslo y recuperemos lo que ha robado."
    },
    {
        "nombre": "La profecia olvidada",
        "descripcion": "Una leyenda habla de un antiguo pergamino que contiene una profecia olvidada. Debemos encontrarlo para descubrir su significado."
    },
    {
        "nombre": "El rescate de la princesa cautiva",
        "descripcion": "La princesa del reino ha sido secuestrada por un malvado hechicero. Debemos rescatarla y devolverla a salvo."
    },
    {
        "nombre": "La busqueda del artefacto perdido",
        "descripcion": "Un artefacto magico de gran poder se ha perdido. Deberemos encontrarlo antes de que caiga en manos equivocadas."
    },
    {
        "nombre": "La venganza del lobo solitario",
        "descripcion": "Un lobo solitario busca vengar la muerte de su manada a manos de cazadores despiadados. Ayudemoslo en su busqueda de justicia."
    },
    {
        "nombre": "El enigma de la estatua llameante",
        "descripcion": "Una estatua en el centro de la ciudad arde en llamas eternas. Descubramos el secreto detras de esta misteriosa estatua."
    },
    {
        "nombre": "El robo del diamante del desierto",
        "descripcion": "Un diamante raro y precioso ha sido robado del desierto. Sigamos las pistas y recuperemos esta valiosa gema."
    },
    {
        "nombre": "La conspiracion en la corte real",
        "descripcion": "Indicios apuntan a una conspiracion en la corte real. Investiguemos para revelar la verdad detras de estos oscuros planes."
    },
    {
        "nombre": "La maldicion del bosque oscuro",
        "descripcion": "Personas han desaparecido misteriosamente en el bosque oscuro. Investiguemos la causa de estas desapariciones."
    },
    {
        "nombre": "La persecucion del ladron maestro",
        "descripcion": "Un ladron maestro ha robado tesoros invaluables. Rastreemoslo y recuperemos lo que ha robado."
    },
    {
        "nombre": "La maldicion del faro embrujado",
        "descripcion": "El faro en la costa esta embrujado por espiritus vengativos. Resolvamos la maldicion que acecha este lugar."
    },
    {
        "nombre": "La venganza del caballero caido",
        "descripcion": "Un caballero noble fue traicionado y exiliado. Descubramos la verdad detras de la traicion y su venganza."
    },
    {
        "nombre": "El dilema de las dos lunas",
        "descripcion": "Dos lunas llenas aparecen en el cielo, un evento raro que trae consigo desafios magicos. Enfrentemos las pruebas y descubramos su significado."
    },
    {
        "nombre": "La busqueda del tesoro maldito",
        "descripcion": "Un antiguo tesoro maldito esta enterrado en una isla remota. Encontremos el tesoro y deshagamonos de su maldicion."
    },
    {
        "nombre": "La venganza del corsario",
        "descripcion": "Un corsario legendario busca vengarse de una traicion. Ayudemoslo a reunir su tripulacion y enfrentar a sus enemigos."
    },
    {
        "nombre": "La busqueda del libro de hechizos",
        "descripcion": "Un libro de hechizos magicos ha desaparecido y podria caer en manos equivocadas. Encontremos el libro antes de que sea demasiado tarde."
    },
    {
        "nombre": "La conspiracion en la corte de las sombras",
        "descripcion": "La corte de las sombras oculta oscuros secretos y complots. Infiltremos la corte y expongamos la conspiracion."
    },
    {
        "nombre": "La defensa de la aldea elfica",
        "descripcion": "Una aldea elfica esta bajo amenaza de un ejercito invasor. Ayudemos a los elfos a defender su hogar."
    },
    {
        "nombre": "El rescate de los prisioneros de guerra",
        "descripcion": "Los prisioneros de guerra necesitan ser rescatados de un campo de batalla. Infiltremos y liberemoslos."
    },
    {
        "nombre": "La venganza de la bruja malvada",
        "descripcion": "Una bruja malvada ha lanzado una maldicion sobre un pueblo. Encontremos a la bruja y pongamos fin a su maleficio."
    },
]

    def getObjectsIds(self, data_base):
        objectsIDs = []
        for collection in ['Consumible', 'Objeto_Clave']:
            objectsIDs.extend([(collection, doc['_id']) for doc in data_base[collection].find({}, projection=["_id"])])
        return objectsIDs

    def generateJsonObj(self, nombre:str, objectsIDs: list, data_base) -> dict[str, Any]:
        equipmentGenerator = EquipmentGenerator()
        etapas_unicas = random.sample(self.etapas_de_mision, 6)
        etapas = [etapas_unicas[index] for index in range(0, random.randint(1,6))]
        recompensas_unicas = random.sample(objectsIDs, 15)
        recompensas = []
        for counter in range(0, random.randint(1, 15)):
            optionPick = random.randint(0, 2)
            if optionPick == 0:
                recompensas.append({"_id": recompensas_unicas[counter][1], "collection": {"$ref": recompensas_unicas[counter][0]}, "cantidad": random.randint(1, 15)})
            elif optionPick == 1:
                recompensas.append(equipmentGenerator.generateEquipmentJsonObj(data_base))
            else:
                recompensas.append(equipmentGenerator.generateWeaponJsonObj(data_base))
        
        return {
            "nombre": nombre,
            "recompensa_xp": random.randint(50, 5201),
            "recompensa_oro": random.randint(10, 1201),
            "recompensa_obj": recompensas,
            "etapas": etapas
        }

    def generateJsonFile(self, registros: dict[str, Any], name:str) -> None:
        def convertir_object_id(obj):
            if isinstance(obj, ObjectId):
                return str(obj)
            raise TypeError
        
        registros_json = json.dumps(registros, indent=4, default=convertir_object_id)
        with open(f'data/{name.lower()}.json', 'w') as archivo_json:
            archivo_json.write(registros_json)


    def generateData(self, name:str, data_base) -> list[dict[str, Any]]:
        objectsIDs = self.getObjectsIds(data_base)
        registros = [self.generateJsonObj(nombre, objectsIDs, data_base) for nombre in self.nombres_de_misiones]
        self.generateJsonFile(registros, name)
        return registros
    
import random, json
from bson import ObjectId
from typing import Any
from . import GeneratorABC, EquipmentGenerator
import time, multiprocessing
from pymongo import MongoClient
import datetime, os

class GeneratorPersonaje(GeneratorABC):
    def __init__(self) -> None:
        self.nombrePersonaje = [
            "DarkKnight123",
            "MageMaster",
            "EpicWarrior",
            "StealthNinja",
            "DragonSlayer",
            "SorcererSupreme",
            "RogueAssassin",
            "HeroicPaladin",
            "MysticMage",
            "LoneWolf",
            "NinjaWarrior",
            "ElvenArcher",
            "DungeonCrawler",
            "ShadowSorcerer",
            "SamuraiMaster",
            "VikingWarlord",
            "MaraudingPirate",
            "CyberPunk404",
            "Spellcaster",
            "TheChosenOne",
            "SwordSage",
            "SteampunkEnthusiast",
            "Mastermind",
            "BardicTroubadour",
            "DwarvenMiner",
            "CunningRogue",
            "WizardryWiz",
            "RoyalKnight",
            "AssassinCreed",
            "WhirlwindWarrior",
            "ElementalMage",
            "RuthlessBandit",
            "PotionBrewer",
            "ValiantValkyrie",
            "BerserkerRage",
            "RangerDanger",
            "MechaMechanic",
            "NobleNecromancer",
            "SpacePilot",
            "PirateCaptain",
            "Swashbuckler",
            "MetalMage",
            "RenaissanceBard",
            "DruidicDancer",
            "MonkMeditator",
            "SpellboundSorcerer",
            "CyberSamurai",
            "LaserLancer",
            "MoonlitMarauder",
            "WandWielder",
            "PandaPirate",
            "CavalierChampion",
            "TechWizard",
            "EagleEyedArcher",
            "WanderingBard",
            "KnightCrusader",
            "DragonRider",
            "ArchMage",
            "SilentShadow",
            "ChronoExplorer",
            "JesterJoker",
            "EternalSoul",
            "DemonHunter",
            "AlchemistAdept",
            "BionicBrigadier",
            "MysticWanderer",
            "ThiefTales",
            "GrandGuardian",
            "LightningLancer",
            "SamuraiSensei",
            "MercilessMercenary",
            "AstralArcher",
            "EtherealEnchanter",
            "PirateProdigy",
            "SorceryScribe",
            "InfernoKnight",
            "TimeTraveler",
            "ShadowSeeker",
            "WizardWarlock",
            "EpicExplorer",
            "RogueRaider",
            "FireBreather",
            "StarshipCaptain",
            "CaptainCourage",
            "WilyWitch",
            "DungeonDelver",
            "WindWalker",
            "MechanicalMaster",
            "MythicMagician",
            "MoonlightMarauder",
            "TheSpellbinder",
            "CyberShogun",
            "StealthySpacefarer",
            "SwordSorcery",
            "GhostPirate",
            "KnightCrusade",
            "SorceressSorcery",
            "SilentNinja",
            "SteampunkScientist",
            "TimeTravelingTitan",
            "NobleNobleman",
            "PiratePower",
            "RogueRuffian",
            "DragonDefender",
            "EtherealEnigma",
            "MysticMysteries",
            "SpellcastingSorcerer",
            "CyberSamuraiX",
            "ArcheryAce",
            "WanderingWarlock",
            "CavalryCaptain",
        ]
        self.lock = ''
        self.queue = ''

    def getObjectsIds(self, data_base):
        inventarioObjectsIDs = []
        for collection in ['Consumible', 'Objeto_Clave']:
            inventarioObjectsIDs.extend([(collection, doc['_id']) for doc in data_base[collection].find({}, projection=["_id"])])
        misionesObjectsIDs = ([("Mision", doc['_id']) for doc in data_base[collection].find({}, projection=["_id"])])
        habilidadesObjectsIDs = [("Habilidad", doc['_id']) for doc in data_base.Habilidad.find({}, projection=["_id"])]
        return (misionesObjectsIDs, inventarioObjectsIDs, habilidadesObjectsIDs)

    def uploadPersonajeData(self, jsonObj, data_base, counterName):
        with self.lock:
            data_base.Personaje.insert_one(jsonObj)

    def generateJsonObj(self, objectsIDs: list, counterName, db_host, db_name) -> dict[str, Any]:
        inicio = time.time()
        cliente = MongoClient(db_host)
        data_base = cliente[db_name]
        equipmentGenerator = EquipmentGenerator()
        inventario = []
        inventario_unicas = random.sample(objectsIDs[1], 50)
        for counter in range(0, random.randint(1, 50)):
            optionPick = random.randint(0, 2)
            if optionPick == 0:
                inventario.append({"_id": inventario_unicas[counter][1], "collection": {"$ref": inventario_unicas[counter][0]}, "cantidad": random.randint(1, 30)})
            elif optionPick == 1:
                inventario.append(equipmentGenerator.generateEquipmentJsonObj(data_base))
            else:
                inventario.append(equipmentGenerator.generateWeaponJsonObj(data_base))
        habilidades = [{"_id": objectsIDs[2][counter][1], "collection": {"$ref": objectsIDs[2][counter][0]}} for counter in range(0, random.randint(1, 20))]
        personajeObj = {
            "nombre": f'{random.choice(self.nombrePersonaje)}{counterName}',
            "nivel": random.randint(1, 100),
            "oro": random.randint(10, 100)*10,
            "puntos_vida": random.randint(10, 80)*10,
            "puntos_accion": random.randint(2, 5),
            "atributos":
                {
                "fuerza": random.randint(10, 100),
                "pericia": random.randint(10, 100),
                "inteligencia": random.randint(10, 100),
                "constitucion": random.randint(10, 100),
                "memoria": random.randint(10, 100),
                "ingenio": random.randint(10, 100),
                "armadura_fisica": random.randint(20, 200),
                "armadura_magica": random.randint(20, 200),
                "movimiento":random.randint(10, 50),
                "iniciativa": random.randint(10, 50),
                "res-fuego":random.randint(0, 100),
                "res-agua":random.randint(0, 100),
                "res-tierra":random.randint(0, 100),
                "res-aire": random.randint(0, 100),
                "res-veneno": random.randint(0, 100),
            },
            "aptitudes": 
                {
                "aeroteurgo":random.randint(1, 20),
                "canalla":random.randint(1, 20),
                "cazador":random.randint(1, 20),
                "contienda":random.randint(1, 20),
                "geomante":random.randint(1, 20),
                "hidrosofista":random.randint(1, 20),
                "invocacion":random.randint(1, 20),
                "necromante":random.randint(1, 20),
                "piroquinectico":random.randint(1, 20),
                "polimorfismo": random.randint(1, 20),
            },
            "habilidades": habilidades,
            "equipo": {
                "armas": [equipmentGenerator.generateWeaponJsonObj(data_base) for counter in range(0, random.randint(1, 2))],
                "equipamiento": [equipmentGenerator.generateEquipmentJsonObj(data_base) for counter in range(0, random.randint(1, 9))],
            },
            "inventario": inventario,
            "misiones": [{"_id": objectsIDs[0][counter][1], "collection": {"$ref": objectsIDs[0][counter][0]}} for counter in range(0, random.randint(1, 10))]
        }
        fin = time.time()
        tiempo_transcurrido_generacion = fin - inicio
        timeValues = list(self.queue.get())
        timeValues[1] += 1
        timeValues[0] += tiempo_transcurrido_generacion
        print(f"Tiempo promedio generacion de Personaje: {round(timeValues[0]/timeValues[1], 2)} s")
        print(f"Tiempo estimado restante: {datetime.timedelta(seconds=round(((timeValues[0]/timeValues[1])*(timeValues[2]-timeValues[1]))/(os.cpu_count() if os.cpu_count() else 4), 0))} s")
        self.queue.put(tuple(timeValues))
        self.uploadPersonajeData(personajeObj, data_base, counterName)
        cliente.close()
        return None

    def generateJsonFile(self, registros: dict[str, Any], name:str) -> None:
        def convertir_object_id(obj):
            if isinstance(obj, ObjectId):
                return str(obj)
            raise TypeError
        
        registros_json = json.dumps(registros, indent=4, default=convertir_object_id)
        with open(f'data/{name.lower()}.json', 'w') as archivo_json:
            archivo_json.write(registros_json)

    def generateData(self, name:str, data_base, db_host, db_name, cantObj: int=10) -> list[dict[str, Any]]:
        inicioTime = time.time()
        objectsIDs = self.getObjectsIds(data_base)
        #self.generateJsonFile(registros, name)
        pool = multiprocessing.Pool()
        manager = multiprocessing.Manager()
        self.lock = manager.Lock()
        self.queue = manager.Queue()
        self.queue.put((0, 0, cantObj))
        totalTimeList = pool.starmap(self.generateJsonObj, [(objectsIDs, counter, db_host, db_name) for counter in range(cantObj)])
        pool.close()
        pool.join() 
        finTime = time.time()
        tiempo_transcurrido_total = finTime - inicioTime
        return tiempo_transcurrido_total
        
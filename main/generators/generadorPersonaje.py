import random, json
from bson import ObjectId
from typing import Any
from . import GeneratorABC, EquipmentGenerator
import multiprocessing

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
        misionesObjectsIDs = ([("Mision", doc['_id']) for doc in data_base.Mision.find({}, projection=["_id"])])
        habilidadesObjectsIDs = [("Habilidad", doc['_id']) for doc in data_base.Habilidad.find({}, projection=["_id"])]
        return (misionesObjectsIDs, inventarioObjectsIDs, habilidadesObjectsIDs)

    def generateJsonObj(self, objectsIDs: list, counterName) -> dict[str, Any]:
        equipmentGenerator = EquipmentGenerator()
        inventario = []
        inventario_unicas = random.sample(objectsIDs[1], min(50, len(objectsIDs[1])))
        for counter in range(0, random.randint(1, len(inventario_unicas))):
            optionPick = random.randint(0, 2)
            elementPick = random.randint(0, len(inventario_unicas)-1)
            if optionPick == 0:
                inventario.append({"_id": inventario_unicas[elementPick][1], "collection": {"$ref": inventario_unicas[elementPick][0]}, "cantidad": random.randint(1, 30)})
            elif optionPick == 1:
                inventario.append(equipmentGenerator.generateEquipmentJsonObj(objectsIDs[2]))
            else:
                inventario.append(equipmentGenerator.generateWeaponJsonObj(objectsIDs[2]))
        habilidades_unicas = random.sample(objectsIDs[2], min(20, len(objectsIDs[2])))        
        habilidades = [{"_id": habilidades_unicas[element][1], "collection": {"$ref": habilidades_unicas[element][0]}} for element in [random.randint(0, len(habilidades_unicas)-1) for counter in range(random.randint(0, len(habilidades_unicas)-1))]]
        misiones_unicas = random.sample(objectsIDs[0], min(20, len(objectsIDs[0])))       
        misiones = [{"_id": misiones_unicas[element][1], "collection": {"$ref": misiones_unicas[element][0]}} for element in [random.randint(0, len(misiones_unicas)-1) for counter in range(random.randint(0, len(misiones_unicas)-1))]]
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
                "armas": [equipmentGenerator.generateWeaponJsonObj(objectsIDs[2]) for counter in range(0, random.randint(1, 2))],
                "equipamiento": [equipmentGenerator.generateEquipmentJsonObj(objectsIDs[2]) for counter in range(0, random.randint(1, 9))],
            },
            "inventario": inventario,
            "misiones": misiones
        }
        print(counterName)
        return personajeObj

    def generateJsonFile(self, registros: dict[str, Any], name:str) -> None:
        def convertir_object_id(obj):
            if isinstance(obj, ObjectId):
                return str(obj)
            raise TypeError
        
        registros_json = json.dumps(registros, indent=4, default=convertir_object_id)
        with open(f'data/{name.lower()}.json', 'w') as archivo_json:
            archivo_json.write(registros_json)

    def generateData(self, name:str, data_base, cantObj: int=10) -> list[dict[str, Any]]:
        objectsIDs = self.getObjectsIds(data_base)
        #self.generateJsonFile(registros, name)
        pool = multiprocessing.Pool()
        manager = multiprocessing.Manager()
        self.lock = manager.Lock()
        self.queue = manager.Queue()
        self.queue.put((0, 0, cantObj))
        personajesObjs = pool.starmap(self.generateJsonObj, [(objectsIDs, counter) for counter in range(cantObj)])
        pool.close()
        pool.join() 
        return personajesObjs

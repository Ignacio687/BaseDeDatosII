import random
from typing import Any

class EquipmentGenerator():
    def __init__(self) -> None:
        self.weapons = [
            ("Espada larga", "Espada", "A una mano"),
            ("Hacha de batalla", "Hacha", "A dos manos"),
            ("Daga", "Cuchillo", "A una mano"),
            ("Arco largo", "Arco", "A distancia"),
            ("Lanza", "Lanza", "A dos manos"),
            ("Martillo de guerra", "Martillo", "A una mano"),
            ("Ballesta", "Arco", "A distancia"),
            ("Cetro mágico", "Vara", "Arma Mágica"),
            ("Hacha arrojadiza", "Hacha", "A distancia"),
            ("Maza", "Maza", "A una mano"),
            ("Bastón de conjuros", "Vara", "Arma Mágica"),
            ("Espada bastarda", "Espada", "A dos manos"),
            ("Dardo venenoso", "Dardo", "A distancia"),
            ("Cimitarra", "Espada", "A una mano"),
            ("Arco corto", "Arco", "A distancia"),
            ("Espada rúnica", "Espada", "Arma Mágica"),
            ("Mandoble", "Espada", "A dos manos"),
            ("Bomba alquímica", "Explosivo", "Arma Mágica"),
            ("Lanza de fuego", "Lanza", "Arma Mágica"),
            ("Vara de relámpagos", "Vara", "Arma Mágica"),
            ("Hacha de tormenta", "Hacha", "Arma Mágica"),
            ("Espada élfica", "Espada", "Arma Mágica"),
            ("Lanza sagrada", "Lanza", "Arma Mágica"),
            ("Báculo de hielo", "Vara", "Arma Mágica"),
            ("Daga sombría", "Cuchillo", "Arma Mágica"),
            ("Arco encantado", "Arco", "Arma Mágica"),
            ("Espada rúnica", "Espada", "Arma Mágica"),
            ("Hacha ancestral", "Hacha", "Arma Mágica"),
            ("Daga venenosa", "Cuchillo", "Arma Mágica"),
            ("Arco élfico", "Arco", "Arma Mágica"),
            ("Lanza de la luz", "Lanza", "Arma Mágica"),
            ("Maza divina", "Maza", "Arma Mágica"),
            ("Cetro arcano", "Vara", "Arma Mágica"),
            ("Espada ancestral", "Espada", "Arma Mágica"),
            ("Hacha de batalla enana", "Hacha", "Arma Mágica"),
            ("Daga de las sombras", "Cuchillo", "Arma Mágica"),
            ("Arco lunar", "Arco", "Arma Mágica"),
            ("Lanza celestial", "Lanza", "Arma Mágica"),
            ("Vara de druida", "Vara", "Arma Mágica"),
            ("Espada rúnica del caos", "Espada", "Arma Mágica"),
            ("Hacha infernal", "Hacha", "Arma Mágica"),
            ("Daga de la noche eterna", "Cuchillo", "Arma Mágica"),
            ("Arco de los susurros", "Arco", "Arma Mágica"),
            ("Lanza de la tormenta", "Lanza", "Arma Mágica"),
            ("Maza sagrada", "Maza", "Arma Mágica"),
            ("Cetro de mago supremo", "Vara", "Arma Mágica"),
            ("Espada del dragón", "Espada", "Arma Mágica"),
            ("Hacha de la muerte", "Hacha", "Arma Mágica"),
            ("Daga de hielo eterno", "Cuchillo", "Arma Mágica"),
            ("Hacha de batalla", "Hacha", "A dos manos"),
            ("Ballesta pesada", "Arco", "A distancia"),
            ("Daga envenenada", "Cuchillo", "A una mano"),
            ("Maza de guerra", "Maza", "A dos manos"),
            ("Arco largo élfico", "Arco", "A distancia"),
            ("Espada rúnica de justicia", "Espada", "A una mano"),
            ("Lanza de los valientes", "Lanza", "A dos manos"),
            ("Hacha del berserker", "Hacha", "A dos manos"),
            ("Vara de los elementos", "Vara", "Arma Mágica"),
            ("Daga arrojadiza de las sombras", "Cuchillo", "A distancia"),
            ("Arco corto reforzado", "Arco", "A distancia"),
            ("Espada encantada de la aurora", "Espada", "A una mano"),
            ("Lanza del dragón", "Lanza", "A dos manos"),
            ("Martillo de guerra enano", "Martillo", "A dos manos"),
            ("Ballesta de repetición", "Arco", "A distancia"),
            ("Daga de cristal", "Cuchillo", "A una mano"),
            ("Maza mágica del sabio", "Maza", "Arma Mágica"),
            ("Arco explosivo", "Arco", "A distancia"),
            ("Hacha de fuego", "Hacha", "A dos manos"),
            ("Daga de hielo", "Cuchillo", "A una mano"),
            ("Espada de la realeza", "Espada", "A una mano"),
            ("Lanza sagrada de los dioses", "Lanza", "A dos manos"),
            ("Maza de tormenta", "Maza", "A dos manos"),
            ("Arco celestial", "Arco", "A distancia"),
            ("Hacha de tormenta", "Hacha", "A dos manos"),
            ("Daga de viento", "Cuchillo", "A una mano"),
            ("Vara ancestral", "Vara", "Arma Mágica"),
            ("Espada maldita", "Espada", "Arma Mágica"),
            ("Lanza ardiente", "Lanza", "A dos manos"),
            ("Maza divina de la justicia", "Maza", "Arma Mágica"),
            ("Arco del cazador", "Arco", "A distancia"),
            ("Hacha del condenado", "Hacha", "Arma Mágica"),
            ("Daga etérea", "Cuchillo", "Arma Mágica"),
            ("Vara de sabiduría", "Vara", "Arma Mágica"),
            ("Espada del dragón de hielo", "Espada", "Arma Mágica"),
            ("Lanza de los elementales", "Lanza", "Arma Mágica"),
            ("Maza de los antiguos", "Maza", "Arma Mágica"),
            ("Arco de la luna dorada", "Arco", "Arma Mágica"),
            ("Hacha del rey enano", "Hacha", "Arma Mágica"),
            ("Daga de los susurros oscuros", "Cuchillo", "Arma Mágica"),
            ("Vara de la magia antigua", "Vara", "Arma Mágica"),
            ("Espada de las almas perdidas", "Espada", "Arma Mágica"),
            ("Lanza de la lluvia de estrellas", "Lanza", "Arma Mágica"),
            ("Maza del juez", "Maza", "Arma Mágica"),
            ("Arco del bosque encantado", "Arco", "Arma Mágica"),
            ("Hacha del lord vampiro", "Hacha", "Arma Mágica"),
            ("Daga del asesino silencioso", "Cuchillo", "Arma Mágica"),
            ("Vara de los dioses olvidados", "Vara", "Arma Mágica")
        ]
        self.description = [
            "El filo de esta arma brilla con un fulgor sobrenatural.",
            "A juzgar por la cantidad de sangre reseca que sube por la empuñadura, parece que esta arma ha visto más de un combate en un pasado no muy lejano.",
            "Los grabados en esta arma cuentan una historia de héroes y leyendas.",
            "El metal de esta arma parece enfriarse en presencia de la magia.",
            "Una runa antigua adorna la hoja de esta arma, otorgándole poderes arcanos.",
            "El peso de esta arma la hace ideal para combates cuerpo a cuerpo.",
            "Una inscripción en una lengua olvidada adorna esta arma.",
            "Las marcas de batalla en esta arma atestiguan su pasado en manos de un guerrero experto.",
            "Un aura mágica rodea esta arma cuando se desenvaina.",
            "El equilibrio de esta arma es perfecto para el combate a dos manos.",
            "La empuñadura de esta arma está envuelta en cuero trenzado para un mejor agarre.",
            "Las gemas incrustadas en esta arma centellean con un resplandor misterioso.",
            "El mango de esta arma está adornado con el símbolo de un antiguo dios.",
            "Esta arma tiene un brillo dorado que la hace parecer divina.",
            "El filo de esta arma es excepcionalmente afilado.",
            "La hoja de esta arma está forjada con acero de alta calidad.",
            "Esta arma emana un frío penetrante.",
            "Las marcas de fuego cubren esta arma, dando la impresión de haber sido templada en el fragor de la batalla.",
            "La madera de la empuñadura de esta arma está ricamente adornada.",
            "El sonido metálico de esta arma al chocar contra otra es ensordecedor.",
            "Esta arma tiene una inscripción en una lengua desconocida que nadie parece poder leer.",
            "Un aura de oscuridad rodea esta arma, emanando un poder siniestro.",
            "Las hojas de esta arma parecen estar envueltas en llamas constantes.",
            "Un grabado de un dragón enroscado adorna el mango de esta arma.",
            "Esta arma brilla intensamente en la oscuridad.",
            "La empuñadura de esta arma está cubierta con escamas de dragón.",
            "Un zumbido eléctrico recorre esta arma cuando se agita.",
            "El filo de esta arma es tan afilado que parece cortar la realidad misma.",
            "Las hojas de esta arma tienen un aspecto resplandeciente como si estuvieran hechas de luz pura.",
            "El ronroneo de un gato se puede escuchar cuando esta arma está desenvainada.",
            "Esta arma tiene un tono dorado que la hace parecer divina.",
            "El filo de esta arma parece ser tan fuerte como el acero en sí.",
            "Las runas talladas en la empuñadura de esta arma otorgan poderes mágicos.",
            "La hoja de esta arma está cubierta de marcas que parecen destellar con electricidad.",
            "Un aura de tranquilidad rodea esta arma.",
            "Las gemas incrustadas en esta arma centellean con una luz calmante.",
            "El sonido metálico de esta arma al chocar contra otra es armonioso.",
            "Esta arma tiene una inscripción en una lengua antigua que solo los sabios pueden leer.",
            "Un aura divina rodea esta arma, emanando un poder sagrado.",
            "El filo de esta arma es tan ligero que parece desafiar la gravedad.",
            "Las hojas de esta arma parecen estar envueltas en llamas divinas.",
            "Un grabado de un fénix en llamas adorna el mango de esta arma.",
            "Esta arma destella intensamente en la luz.",
            "La empuñadura de esta arma está envuelta en plumas de ángel.",
            "Un sonido celestial se puede escuchar cuando esta arma está desenvainada.",
            "Esta arma tiene un tono plateado que la hace parecer sagrada.",
            "El filo de esta arma parece ser tan afilado como la misma realidad.",
            "Las runas talladas en la empuñadura de esta arma otorgan poderes divinos.",
            "La hoja de esta arma está cubierta de marcas que parecen destellar con luz celestial.",
            "Un aura de paz rodea esta arma.",
            "Las gemas incrustadas en esta arma centellean con una luz celestial.",
            "El sonido metálico de esta arma al chocar contra otra es angelical.",
            "Esta arma tiene una inscripción en una lengua sagrada que solo los elegidos pueden leer.",
            "A juzgar por la cantidad de sangre reseca que subre la empunadura, parece que esta arma ha visto mas de un combate en un pasado no muy lejano."
        ]
        self.equipment = [
            ("Yelmo del Último Rey Hechicero de la Fuente", "Casco", "El yelmo del último rey hechicero de la Fuente es temible e imponente. Ya no pesa sobre él ningún antiguo mal y no supone una amenaza directa para su portador. Aunque, ¿quién sabe lo que podrían llegar a hacerte quienes se ofendan por tu elección de vestuario?"),
            ("Pechera de Placas de Dragón", "Pechera", "Esta pechera de placas forjada a partir de escamas de dragón es prácticamente impenetrable. Se rumorea que otorga al portador la resistencia de un dragón."),
            ("Guantes del Mago Arcano", "Guantes", "Estos guantes de seda negra están bordados con runas arcanas. Mejoran la destreza mágica y permiten lanzar hechizos con mayor facilidad."),
            ("Botas del Viajero", "Botas", "Las botas del viajero son ideales para largos recorridos a pie. Son resistentes, cómodas y permiten al portador caminar largas distancias sin fatigarse."),
            ("Anillo de Invisibilidad", "Anillo", "Este anillo concede al portador la habilidad de volverse invisible a voluntad. Ideal para situaciones sigilosas."),
            ("Collar de Protección Divina", "Collar", "Este collar bendecido por los dioses otorga protección contra el mal y maldiciones. Es una joya sagrada."),
            ("Yelmo del Caballero Valiente", "Casco", "El yelmo del caballero valiente es conocido por su diseño elegante y resistencia. Fue usado por un héroe legendario en muchas batallas."),
            ("Pechera de Placas del Guardián", "Pechera", "Esta pechera de placas es el emblema de los guardianes del reino. Brinda una defensa inquebrantable y nobleza en el campo de batalla."),
            ("Guantes del Ladrón Astuto", "Guantes", "Estos guantes son perfectos para los ladrones y bandidos. Mejoran la habilidad para abrir cerraduras y deslizarse en las sombras."),
            ("Botas de Salto Élfico", "Botas", "Las botas de salto élfico permiten a su portador dar saltos increíbles y moverse con agilidad. Son populares entre los arqueros."),
            ("Anillo de Regeneración", "Anillo", "Este anillo acelera la regeneración natural del cuerpo. Las heridas sanan más rápido y la fatiga se desvanece."),
            ("Collar de la Luna Plateada", "Collar", "El collar de la luna plateada emana un brillo mágico. Los poderes de la luna favorecen al portador en la noche."),
            ("Yelmo de los Antiguos Reyes", "Casco", "Este yelmo lleva grabados los nombres de los antiguos reyes. Otorga sabiduría y coraje a quien lo lleva."),
            ("Pechera de Placas del General", "Pechera", "La pechera del general es un símbolo de liderazgo en el ejército. Quien la lleve inspirará valor a sus camaradas."),
            ("Guantes de Fuego", "Guantes", "Estos guantes están imbuidos con el poder del fuego. Permiten al portador lanzar bolas de fuego a sus enemigos."),
            ("Botas de Caminante de la Montaña", "Botas", "Las botas de caminante de la montaña brindan estabilidad en terrenos accidentados y permiten escalar montañas con facilidad."),
            ("Anillo del Señor de las Bestias", "Anillo", "Este anillo concede al portador la habilidad de comunicarse con y controlar a las bestias salvajes."),
            ("Collar de las Estrellas", "Collar", "El collar de las estrellas brilla en la oscuridad y permite al portador navegar por la noche con facilidad."),
            ("Yelmo del Lobo", "Casco", "Este yelmo tiene la forma de la cabeza de un lobo y otorga al portador la astucia de este depredador."),
            ("Pechera de Placas de Titanio", "Pechera", "Esta pechera de placas hecha de titanio es extremadamente resistente y ligera. Ideal para la movilidad en el campo de batalla."),
            ("Guantes de Hielo", "Guantes", "Estos guantes están imbuidos con el poder del hielo. Permite al portador congelar a sus enemigos con un toque."),
            ("Botas de Corredor Veloz", "Botas", "Las botas de corredor veloz otorgan velocidad sobrenatural al portador, permitiéndole moverse a una velocidad vertiginosa."),
            ("Anillo del Sabio", "Anillo", "Este anillo otorga conocimiento y sabiduría a quien lo lleva. Sus decisiones serán siempre las más acertadas."),
            ("Collar del Océano Profundo", "Collar", "El collar del océano profundo permite al portador respirar bajo el agua y explorar los misterios del mar."),
            ("Yelmo del Dragón", "Casco", "Este yelmo está adornado con la forma de un dragón. Quienes lo lleven obtienen la fuerza y el poder de este legendario ser."),
            ("Pechera de Placas del Cazador", "Pechera", "La pechera del cazador está diseñada para acechar a las bestias salvajes. Quien la lleve tendrá éxito en la caza."),
            ("Guantes de los Vientos", "Guantes", "Estos guantes permiten al portador controlar los vientos y volar brevemente. Ideales para la exploración aérea."),
            ("Botas del Oso", "Botas", "Las botas del oso otorgan al portador la fuerza de un oso. Sus pisadas son temibles."),
            ("Anillo de la Armonía", "Anillo", "Este anillo otorga paz y armonía a su portador. Las emociones y el estrés desaparecen."),
            ("Collar del Bosque Encantado", "Collar", "El collar del bosque encantado permite al portador comunicarse con las criaturas del bosque y ganarse su ayuda."),
            ("Yelmo del Sabio Magus", "Casco", "Este yelmo está adornado con runas mágicas. Otorga un mayor control sobre la magia y el conocimiento arcano."),
            ("Pechera de Placas del Heraldo", "Pechera", "La pechera del heraldo lleva el escudo del reino. Es símbolo de honor y deber."),
            ("Guantes de la Sombra", "Guantes", "Estos guantes permiten al portador esconderse en las sombras y moverse sin ser detectado."),
            ("Botas del Nómada", "Botas", "Las botas del nómada son ideales para viajar largas distancias en terrenos diversos. Son resistentes y cómodas."),
            ("Anillo del Alquimista", "Anillo", "Este anillo otorga al portador el conocimiento de la alquimia y la capacidad de crear pociones mágicas."),
            ("Collar del Astrónomo", "Collar", "El collar del astrónomo permite al portador explorar el cielo nocturno y entender los secretos de las estrellas."),
            ("Yelmo del Luchador Valiente", "Casco", "El yelmo del luchador valiente es conocido por su resistencia en la arena de combate. Ha sido testigo de innumerables duelos."),
            ("Pechera de Placas del Héroe", "Pechera", "Esta pechera de placas ha sido usada por héroes legendarios. Quienes la lleven inspirarán coraje a sus aliados."),
            ("Guantes del Hechicero", "Guantes", "Estos guantes están tejidos con hilos mágicos que mejoran la capacidad del portador para lanzar hechizos."),
            ("Botas del Cazador", "Botas", "Las botas del cazador otorgan agilidad y velocidad al portador. Ideales para perseguir a las bestias."),
            ("Anillo de la Llama Eterna", "Anillo", "Este anillo está imbuido con el poder de una llama que nunca se apaga. Permite al portador lanzar llamas con un gesto."),
            ("Collar del Guardian del Templo", "Collar", "El collar del guardián del templo es símbolo de protección y lealtad. Otorga resistencia contra el mal."),
            ("Yelmo del Rey Guerrero", "Casco", "Este yelmo lleva el sello de un antiguo rey guerrero. Otorga fuerza y liderazgo a quien lo lleve."),
            ("Pechera de Placas del Caballero", "Pechera", "La pechera de placas del caballero es conocida por su resistencia y nobleza en el campo de batalla."),
            ("Guantes de la Destreza", "Guantes", "Estos guantes permiten al portador realizar movimientos precisos y mortales en el combate."),
            ("Botas del Sigilo", "Botas", "Las botas del sigilo permiten al portador moverse en silencio y pasar desapercibido en la oscuridad."),
            ("Anillo del Dragón de Oro", "Anillo", "Este anillo está adornado con una gema que brilla como el oro. Otorga al portador la fuerza de un dragón dorado."),
            ("Collar de la Serpiente de Jade", "Collar", "El collar de la serpiente de jade otorga al portador la sabiduría de las serpientes y la capacidad de hablar con ellas."),
        ]

    def generateWeaponJsonObj(self, data_base) -> dict[str, Any]:
        habilidadesIDs = [("Habilidad", doc['_id']) for doc in data_base.Habilidad.find({}, projection=["_id"])]
        habilidades = [{"_id": habilidadesIDs[counter][1], "collection": {"$ref": habilidadesIDs[counter][0]}} for counter in range(0, random.randint(1, 3))]
        rarezas = ["Poco común", "Común", "Inusual", "Rara", "Épica", "Legendaria", "Mítica"]
        requerimientos = ["fuerza", "pericia", "inteligencia", "constitución", "memoria", "ingenio"]
        weapon = random.choice(self.weapons)
        weaponObj = {
            "nombre": weapon[0],
            "arma": weapon[1],
            "tipo": weapon[2],
            "dano-min": random.randint(5, 43),
            "dano-max": random.randint(45, 151),
            "critico": random.randint(180, 361),
            "puntos_de_accion": random.randint(1, 6),
            "nivel": random.randint(1, 51),
            "peso": round(random.uniform(0.5, 16), 2),
            "valor": random.randint(10, 35000),
            "rareza": random.choice(rarezas),
            "alcance": round(random.uniform(0.1, 7), 1),
            "efectos": [{habilidad: random.randint(1, 3)} for habilidad in requerimientos],
            "requerimiento": [
                {
                    random.choice(requerimientos): random.randint(1, 21)
                }
            ],
            "habilidad": habilidades,
            "descripcion": random.choice(self.description)
        }
        return weaponObj
    
    def generateEquipmentJsonObj(self, data_base) -> dict[str, Any]:
        habilidadesIDs = [("Habilidad", doc['_id']) for doc in data_base.Habilidad.find({}, projection=["_id"])]
        habilidades = [{"_id": habilidadesIDs[counter][1], "collection": {"$ref": habilidadesIDs[counter][0]}} for counter in range(0, random.randint(1, 3))]
        rarezas = ["Poco común", "Común", "Inusual", "Rara", "Épica", "Legendaria", "Mítica"]
        requerimientos = ["fuerza", "pericia", "inteligencia", "constitución", "memoria", "ingenio"]
        equipment = random.choice(self.equipment)
        equipmentObj = {
            "nombre": equipment[0],
            "tipo": equipment[1],
            "nivel": random.randint(1, 51),
            "peso": round(random.uniform(0.5, 16), 2),
            "valor": random.randint(10, 35000),
            "rareza": random.choice(rarezas),
            "armadura fisica": random.randint(1, 100),
            "armadura_magica": random.randint(1, 100),
            "descripcion": equipment[2],
            "efectos":[{habilidad: random.randint(1, 3)} for habilidad in requerimientos],
            "requerimiento": [
                {
                    random.choice(requerimientos): random.randint(1, 21)
                }
            ],
            "habilidad": habilidades
        }
        return equipmentObj

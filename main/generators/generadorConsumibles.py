import json
import random
import pymongo

cliente = pymongo.MongoClient("mongodb+srv://Cluster18604:mati2002@cluster0.zale6eu.mongodb.net/")
db = cliente.MMO_RPG  # Reemplaza "tu_base_de_datos" con el nombre de tu base de datos
coleccion = db.Consumibles  # Reemplaza "tu_coleccion" con el nombre de tu colección


def generador_objetos_consumible():
    tipos_objetos = ["pocion", "pan", "bomba molotov", "elixir", "piedra preciosa", "pergamino", "pocion de invisibilidad", "pocion de fuerza", "pocion de velocidad", "pocion de resistencia", "pocion de salud", "pocion de mana", "pocion de veneno", "pocion de fuego", "pocion de hielo", "pocion de electricidad", "pocion de curacion", "pocion de regeneracion"]
    adjetivos = ["poderoso", "magico", "encantado", "antiguo", "legendario", "oscuro", "resplandeciente", "divino", "caotico", "misterioso", "raro", "comun", "incomun", "epico", "unico", "maldito"]
    consumibles = []

    for tipo in tipos_objetos:
        for adjetivo in adjetivos:
            atributos = ["Agilidad", "Inteligencia", "Resistencia", "Suerte", "Carisma", "Sabiduria", "Destreza", "Constitucion", "Percepcion", "Voluntad"]
            peso = round(random.uniform(0.01, 2), 2) 
            valor = random.randint(10, 100) 
            descripcion = f"Este/a {tipo} {random.choice([ 'tiene propiedades magicas', 'viene de un reino muy lejano', 'pertenece a una dinastia perdida', 'lo encontaste en el suelo', 'se uso en la guerra contra los elfos', 'fue conseguido tras derramar mucha sangre', 'se lo saco dios de dios sabe donde', 'parece bastante normal'])} y es {random.choice(['muy poderoso', 'antiguo, de una era olvidada', 'misterioso', 'un invento de la iglesia catolica', 'un objeto maldido', 'esencial para la supervicenai de los 7 reinos', 'mortal, en las manos adecuadas'])}." 
            
            efectos = []
            for index in range(1, random.randint(2,6)):
                efecto = random.choice(atributos)
                if efecto not in [list(efecto.keys())[0] for efecto in efectos]:
                    efectos.append({efecto: random.randint(1, 15)})
            duracion = random.randint(1, 10)  # Duración aleatoria entre 1 y 10

            consumibles.append({
                "tipo": tipo,
                "nombre": f'{adjetivo} {tipo}',
                "peso": peso,
                "valor": valor,
                "descripcion": descripcion,
                "efectos": efectos,
                "duracion": duracion
            })

    return consumibles

objetos_consumibles_json = json.dumps(generador_objetos_consumible(), indent=4)

with open('data/objetos_consumibles.json', 'w') as archivo_json:
    archivo_json.write(objetos_consumibles_json)

print("Datos generados y guardados en objetos_consumibles.json")
print("#"*10)
entrada= input("# Presiona ENTER para Cargar a la base")
print("#"*10)
if entrada:
    with open('data/objetos_consumibles.json', 'r') as archivo_json:
        datos_json = json.load(archivo_json)
    coleccion.insert_many(datos_json)
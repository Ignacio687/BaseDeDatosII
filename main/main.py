import json
import random
import pymongo

cliente = pymongo.MongoClient("mongodb://tu_usuario:tu_contraseña@tu_direccion_del_servidor:puerto/tu_base_de_datos")
db = cliente.tu_base_de_datos  # Reemplaza "tu_base_de_datos" con el nombre de tu base de datos
coleccion = db.tu_coleccion  # Reemplaza "tu_coleccion" con el nombre de tu colección


def generar_objeto_consumible():
    tipos_objetos = ["pocion", "pan", "bomba molotov", "elixir", "piedra preciosa", "pergamino", "pocion de invisibilidad", "pocion de fuerza", "pocion de velocidad", "pocion de resistencia", "pocion de salud", "pocion de mana", "pocion de veneno", "pocion de fuego", "pocion de hielo", "pocion de electricidad", "pocion de curacion", "pocion de regeneracion"]
    tipo = random.choice(tipos_objetos)
    adjetivos = random.choice(["poderoso", "magico", "encantado", "antiguo", "legendario", "oscuro", "resplandeciente", "divino", "caotico", "misterioso", "raro", "comun", "incomun", "epico", "unico", "maldito"])
    nombre = f"{adjetivos} {tipo}"
    peso = round(random.uniform(0.01, 2), 2) 
    valor = random.randint(10, 100) 
    descripcion = f"Este/a {tipo} {random.choice([ 'tiene propiedades magicas', 'viene de un reino muy lejano', 'pertenece a una dinastia perdida', 'lo encontaste en el suelo'])} y es {random.choice(['muy poderoso', 'antiguo', 'raro', 'misterioso', 'poco comun', 'sucio'])}." 
    efectos = [{"Fuerza": random.randint(1, 5)}] 
    duracion = random.randint(1, 10) 
    objeto_consumible = {
        "tipo": tipo,
        "nombre": nombre,
        "peso": peso,
        "valor": valor,
        "descripcion": descripcion,
        "efectos": efectos,
        "duracion": duracion
    }
    return objeto_consumible
objetos_consumibles = [generar_objeto_consumible() for _ in range(100)]

objetos_consumibles_json = json.dumps(objetos_consumibles, indent=4)

with open('data/objetos_consumibles.json', 'w') as archivo_json:
    archivo_json.write(objetos_consumibles_json)

print("Datos generados y guardados en objetos_consumibles.json")
entrada= input("PRESIONA ENTER PARA EXPLOTAR")
if entrada or not entrada:
    with open('objetos_consumibles.json', 'r') as archivo_json:
        datos_json = json.load(archivo_json)
    coleccion.insert_many(datos_json)
from main.generateDataBase import DataBaseGenerator

if __name__ == "__main__":
    app = DataBaseGenerator("mongodb+srv://Cluster18604:mati2002@cluster0.zale6eu.mongodb.net/")
    colecciones = ['Habilidad', 'Consumible', 'Objeto_Clave', 'Mision', 'Personaje']
    lista_numerada = [f'{index + 1} - {elemento}' for index, elemento in enumerate(colecciones)]
    userInput = input('Desea eliminar la base de datos existente?(y/n)')
    if userInput == "y":
        app.setDeleteDBFlag(True)
    elif input('Desea eliminar las colecciónes existentes?(y/n)') == 'y':
        app.setDeleteColectionFlag(True)
    while True:
        print("Que colecciones desea generar: ")
        print("0 - Todas las colecciones")
        for item in lista_numerada:
            print(item)
        userInput = input("Opcion:   ")
        if userInput == "0":
            app.setDBCollections(colecciones)
            break
        elif userInput in ['1', '2', '3', '4', '5']:
            app.setDBCollections([colecciones[int(userInput) - 1]])
            break
    while True:
        userInput = input('Catidad de personajes:  ')
        if userInput.isdigit():
            app.setcantPersonajes(int(userInput))
            break
    app.setDBName("MMO_RPG1")
    app.generateDB()
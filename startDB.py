from main.generateDataBase import DataBaseGenerator

if __name__ == "__main__":
    app = DataBaseGenerator("mongodb://127.0.0.1:27017/")#('mongodb://localhost:27017')
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
    app.setDBName("MMO_RPG")
    app.generateDB()
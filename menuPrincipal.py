import crud #Importames el archivo de crud para las funciones

opcion = 0 #Para el menu
continuar = True #Para salir del menu

while continuar:
    try:
        print("******** MENU ZOOLOGICO********")
        print("1. Crear un nueva tabla (CREATE)")
        print("2. Ingresar un nuevo Zoo (CREATE Y READ)")
        print("3. Eliminar una especie de un zoo (DELETE Y READ)")
        print("4. Actualizar datos de Zoo (update)")
        print("5. Salir")
        opcion = int(input("Ingresa una opcion: "))
    except:
        print(" ****** VALOR INVALIDO ******")
    else:
        match(opcion):
            case 1:
                """ Enviar al formulario de crear un nueva tabla a crud"""
                crud.crearTabla()
            case 2:
                crud.crearZoo()
            case 3:
                crud.eliminiarEspecie()
            case 4:
                crud.modificarZoo()
            case 5:
                continuar =False
            case _:
                print("Valor ingresado no valido")

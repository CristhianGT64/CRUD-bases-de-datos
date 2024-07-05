import crud #Importames el archivo de crud para las funciones

opcion = 0 #Para el menu
continuar = True #Para salir del menu

while continuar:
    try:
        print("******** MENU ZOOLOGICO********")
        print("1. Crear un nueva tabla (CREATE)")
        print("2. Mostrar todos los productos")
        print("3. Mostrar un producto")
        print("4. Ingresar al inventario")
        print("5. Quitar del inventario")
        print("6. Salir")
        opcion = int(input("Ingresa una opcion: "))
    except:
        print(" ****** VALOR INVALIDO ******")
    else:
        match(opcion):
            case 1:
                """ Enviar al formulario de crear un nueva tabla a crud"""
                crud.crearTabla()
            case 6:
                continuar =False
            case _:
                print("Valor ingresado no valido")

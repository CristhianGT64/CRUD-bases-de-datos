opcion = 0
contador = 0
continuar = True

while continuar:
    try:
        print("******** MENU ********")
        print("1. Ingresar un producto")
        print("2. Mostrar todos los productos")
        print("3. Mostrar un producto")
        print("4. Ingresar al inventario")
        print("5. Quitar del inventario")
        print("6. Salir")
        opcion = int(input("Ingresa una opcion: "))
    except:
        print(" ****** VALOR INVALIDO ******")
    else:
        print(False)
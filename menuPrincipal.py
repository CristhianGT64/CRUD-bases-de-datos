import crud #Importames el archivo de crud para las funciones


def menuPrincipal (conexion):
    opcion = 0 #Para el menu
    continuar = True #Para salir del menu
    while continuar:
        try:
            print("******** MENU ZOOLOGICO********")
            print("1. Crear un nueva tabla (CREATE)")
            print("2. Ingresar un nuevo Zoo")
            print("3. Eliminar una especie de un zoo")
            print("4. Actualizar datos de Zoo")
            print("5.Leer datos de la tablas")
            print('6. Otorgar Permisos')
            print('7. Quitar Permisos')
            print('8. Crear un nuevo usuario')
            print("9. Alterar una tabla")
            print("10. Eliminar una tabla")
            print("11. Salir")
            opcion = int(input("Ingresa una opcion: "))
        except:
            print(" ****** VALOR INVALIDO ******")
        else:
            match(opcion):
                case 1:
                    """ Enviar al formulario de crear un nueva tabla a crud"""
                    crud.crearTabla(conexion) #Dinamica con conexion
                case 2:
                    crud.crearZoo(conexion)
                case 3:
                    crud.eliminiarEspecie(conexion)
                case 4:
                    crud.modificarZoo(conexion)
                case 5:
                    print("********* Tablas de la base de Datos disponible (READ)************")
                    crud.viewTables(conexion)
                    nameTable = input("Elija el nombre de la tabla que desear leer sus datos(Read): ")
                    print("\n")
                    crud.select_table(nameTable, conexion)
                    print("\n")    
                case 6:
                    print('si')
                case 9:
                    crud.alterTable(conexion)
                case 10:
                    crud.dropTableFunction(conexion)
                case 11:
                    continuar =False
                case _:
                    print("Valor ingresado no valido")

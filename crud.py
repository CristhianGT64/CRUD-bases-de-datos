from xmlrpc.client import boolean
import conexionDB as cbd 
""" Importamos del archivo que hacemos nuestra conexion como cbd = conexion base de datos """

""" Variables globales """


def encederConexion(conexion):
    # conexion = cbd.iniciarConexion() #Decimos que conexion es igual al objeto de la conexion para instanciarlo
    cur = conexion.cursor() #Crearemos un cursor que nos permite manipular nuestra base de datos
    return cur

def apagarConexion(cur):
    cur.close()

""" Universal para todo el crud, una vez teniendo el query se llama esta funcion """
def impactarDB(query, conexion, accion = None):
    cur = conexion.cursor()
    cur.execute(query)  #Mandar la consulta
    if accion == 'consultas' :
        consulta = cur.fetchall() #Ejecutar la consulta para leer y trael lo que consigue (Aqui hacemos el READ)
        return consulta
    cur.commit() #Ejecutar la consulta
    cur.close()


""" Recorrer la lista para generar el query de crear """
def crear(nombreTabla, llavePrimaria, cur, campos):
    """ query para crear tablas """
    query = "CREATE TABLE " + nombreTabla + " ( "
    query += llavePrimaria + ' INTEGER PRIMARY KEY, ' #Determinar la llave primaria

    """ Ingresar al query los campos y su valor """
    
    for vercampos in campos: #Recorremos la lista o arreglo donde estan los campos
        for valorCampo in vercampos.values(): #Recorremos los diccionarios para obtener los valores de los campos
                query += valorCampo + ' '
        query += ', ' #Ponemos una , despues de cada campo
    query += ' );' #Cerramos todo
    
    """ Impactamos la base de datos con el query que generamos con valores ingresados por el usuario"""
    try:
        impactarDB(query, cur)
        print(' -------> Se creo la tabla correctamente <----------')
    except :
        print('No se pudo ejecutar el query, revisa que los tipos de datos esten bien escritos' )

""" Conseguir informacion de las ciudades disponibles en la base de datos """
def informacionCiudades(cur):
    # cur = encederConexion() #Traemos el cursos para hacer modficaciones en la base de datos
    query = 'SELECT * FROM ciudades'
    return impactarDB(query,cur, 'consultas')

def informacionZoo(cur):
    # cur = encederConexion() #Traemos el cursos para hacer modficaciones en la base de datos
    query = 'SELECT * FROM zoologicos'
    return impactarDB(query,cur, 'consultas')

def informacionZooEspecifico(idZoo, cur):
    # cur = encederConexion() #Traemos el cursos para hacer modficaciones en la base de datos
    query = 'SELECT * FROM zoologicos where idZoo = ' + str(idZoo)
    return impactarDB(query,cur, 'consultas')

def modificar(atributo,nvoDato, idZoo , cur):
    # cur = encederConexion() #Traemos el cursos para hacer modficaciones en la base de datos
    query = f"UPDATE zoologicos SET {str(atributo)} = '{str(nvoDato)}' where idZoo = {str(idZoo)}"
    return impactarDB(query,cur, 'Actualizar')


def informacionAnimales(cur):
    # cur = encederConexion() #Traemos el cursos para hacer modficaciones en la base de datos
    query = 'SELECT * FROM especieAnimales'
    return impactarDB(query,cur, 'consultas')


def InformacionAnimalZoo(numZoo, cur):
    # cur = encederConexion() #Traemos el cursos para hacer modficaciones en la base de datos
    query = 'SELECT * FROM espciesZoologicos WHERE idZoo = ' + str(numZoo)
    return impactarDB(query,cur, 'consultas')

def realizarInsert(lista, nombreTabla, cur):
    # cur = encederConexion()
    query = 'INSERT INTO ' + nombreTabla + ' VALUES ( '
    for i, datos in enumerate(lista):
        query += str(datos)
        if (i < len(lista) - 1):
            query += ', '
    query += ' );'
    impactarDB(query, cur)
    print(' ---Ingresado correctamente--- ')

def realizarDelete(tabla, codigozoo, codigoAnimal, cur):
    # cur = encederConexion()
    query = f' DELETE FROM  {tabla} where idEspecie = {str(codigoAnimal)} and idZoo = {str(codigozoo)}'
    # print(query)
    return impactarDB(query,cur, 'Eliminar')

def addColumn(cur, table_name, column_name, column_type):
    # cur = encederConexion()
    query = f"ALTER TABLE {table_name} ADD {column_name} {column_type}"
    print(query)
    return impactarDB(query,cur, 'Actualizar')

def dropColumn(cur, table_name, column_name):
    # cur = encederConexion()
    query = f"ALTER TABLE {table_name} DROP COLUMN {column_name}"
    return impactarDB(query,cur, 'Actualizar')

def dropTable(cur, table_name):
    # cur = encederConexion()
    query = f"DROP TABLE {table_name}"
    return impactarDB(query,cur, 'Eliminar')

""" Pedir datos al usuario """
def crearTabla(cur):
    """ Encedemos la conexion con la base de datos """
    # cur = encederConexion() #Traemos el cursos para hacer modficaciones en la base de datos
    campos = []
    opcion = ""
    continuar = True

    nombreTabla = input("Ingresa el nombre de la tabla nueva: ")
    llaveprimaria = input("Nombre de llave Primaria: ")
    """ Dejaremos que por defaul sea Integer """

    """ Permite meter al usuario la cantidad de campos que necesite """
    while continuar:
            nvoCampo = {} ##Usaremos diccionarios para guardar campos y valores como clave valor
            nvoCampo['nombreCampo'] = input("Ingrese el nombre del campo: ")
            nvoCampo['tipoDato'] = input("Ingresa en tipo de dato (Por ejemplo VARCHAR(55) o INTENGER): ")
            campos.append(nvoCampo)
            try:
                opcion = int(input('Si desea agregar mas presione 1, si desea terminar presione 2, si desea salir y no guardar cambios presione 3 \n --->'))
            except:
                print("Valores incorrectos") 
            else:
                 match(opcion):
                        case 1:
                         continue #Continua y permite ingresar mas campos (Si va un campo malo despues afectara)
                        case 2:
                           crear(nombreTabla, llaveprimaria, cur, campos) #Esta funcion tendra el query para crear la tabla
                           continuar = False
                        case 3:
                           continuar = False
                        case _:
                           print('Valor ingresado no valido, Volviendo al menu principal... ')
                           continuar = False

def crearZoo(cur):
    tuplas = []
    contador = 0
    numCiudad = 0
    try:
        tuplas.append(input('Ingresa el Id del Zoo --->'))
        nombre = (input('Ingresa en nombre del Zoo --->'))
        tuplas.append(" ' " + nombre + " ' ")
        tuplas.append(float(input('Ingresa el tamanio del zoologico --->')))
        tuplas.append(float(input('Ingresa el presupuesto--->')))
        print('Ciudad que se encuentra el zoo, usa cualquiera de la siguientes opciones')
        ciudades = informacionCiudades(cur)
        print('Se encontraron las ciudades')
        for ciudad in ciudades:
            print(f'{ciudad.idCiudad} ) {ciudad.nombre}') #recorremos las ciudades para elegir uno
            contador += 1
        while (numCiudad <= 0 or numCiudad > contador):
            numCiudad = int(input('Ingresa el numero de la ciudad  ---> '))
            if( numCiudad <= 0 or numCiudad > contador ):
                print('Valor ingresado no valido, porfavor vuelve a intentarlo')
        tuplas.append(numCiudad)
        # print(tuplas)
        realizarInsert(tuplas, 'zoologicos', cur)
        print('Se ingreso el zoologico correctamente')
    except :
        print('Valor incorrecto o no valido')


def eliminiarEspecie(cur):
    codigosZoo = []
    codigoAnimal = []
    numZoo = 0
    numAnimal = 0
    seguir = True
    try:
        print('Selecciona un zoologico')
        zoologicos = informacionZoo(cur) #Mandar a llamar los zoo en db
        for zoo in zoologicos: #Recorrer la lista de zoo
            print(f'{zoo.idZoo} ) {zoo.nombre}') #recorremos las ciudades para elegir uno
            codigosZoo.append(zoo.idZoo)
        while seguir:
            numZoo = int(input('Ingresa el numero de la ciudad  ---> '))
            if( numZoo in codigosZoo ):
                print('Existe el codgio en la lista')
                animalxZoo = InformacionAnimalZoo(numZoo, cur)
                animales = informacionAnimales(cur)
                print('Animales disponibles: ')
                for animalzoo in animalxZoo: #Ingresamos que animales estan en el zoo que se eligio
                    codigoAnimal.append(animalzoo.idEspecie)
                print(codigoAnimal)
                for animal in animales:
                    print(f'{animal.idEspecie} ) Nombre Vulgar: {animal.nombreVulgar}')
                while True:
                    numAnimal = int(input('Ingrese el codigo del animal -->'))
                    if(numAnimal in codigoAnimal):
                        print('Se encontro el animal en el zoo, eliminando...')
                        realizarDelete("espciesZoologicos", numZoo, numAnimal, cur)
                        print('Se quito el animal del zoo')
                        break;
                    else:
                        print('Este animal no esta disponible en este zoo')


                seguir = False
            else:
                print('No existe el codigo en la lista')
    except :
        print('No se ingresaron los valores correctamente')


def modificarZoo(cur):
    codigosZoo = []
    actu = 0
    atributo = ""
    nvoValor = ''
    try:
        print('Selecciona el Zoologico a modificar, usa cualquiera de la siguientes opciones')
        zoologicos = informacionZoo(cur)
        for zoo in zoologicos: #Recorrer la lista de zoo
            print(f'{zoo.idZoo} ) {zoo.nombre}') #recorremos las ciudades para elegir uno
            codigosZoo.append(zoo.idZoo)
        while True:
            idZoo = int(input('Ingresa el numero del Zoo  ---> '))
            if (idZoo in codigosZoo):
                print('Informacion actual de zoo:')
                zoo = informacionZooEspecifico(idZoo, cur)
                """ hacer menu para que elija que actualizar """
                try:
                    print(f'Nombre zoo:{zoo[0].nombre} tamanio: {zoo[0].tamanio} presupuesto: {zoo[0].presupuesto}')
                    print('Modificar: \n 1)nombre\n2)Tamanio\n3)presupuesto')
                    actu = int(input('--->'))
                except :
                    print('No se pudo actualizar el registro')
                else:
                    match(actu):
                        case 1 :
                            nvoValor = input('Ingresa el nuevo Nombre del Zoo -->')
                            atributo = "nombre"
                        case 2:
                            nvoValor = float(input('Ingresa el nuevo tamanio del Zoo -->'))
                            atributo = "tamanio"
                        case 3:
                            nvoValor = float(input('Ingresa el presupuesto Nombre del Zoo -->'))
                            atributo = "presupuesto"
                        case _:
                            print('Dato ingresado no valido')
                    modificar(atributo, nvoValor, idZoo, cur)
                    print('Se actualizaron los datos correctamente')
                break;
            else:
                print('No se encontro el zoo')

        # modificarZoo(idZoo)
    except :
        print('No se ingresaron los valores correctamente')

def encabezadoTablas(query, conexion):
    cur = encederConexion(conexion)
    cur.execute(query)
    encabezado = cur.description
    apagarConexion(cur)
    return encabezado

def viewTables(cur):
    # cur = encederConexion();
    contador=1;
    try:       
       #Consulta que muestra el nombre de todas las tablas de la base de datos  
        query = "SELECT table_name FROM information_schema.tables WHERE table_type ='BASE TABLE';"
        
        #Realizar la consulta
        tables=impactarDB(query,cur,"consultas")
        for table in tables:
            print(f'{contador} ) {table.table_name}')
            contador +=1;
            
    except:
        print('Error en leer las tablas')

def select_table(table_name, conexion):
    # cur = encederConexion(conexion);
    try:        
        select_query = f"SELECT * FROM {table_name}"   

        filas= impactarDB(select_query,conexion,'consultas')
        
        #Obtener lista de nombre del encabezado de la tabla
        nameEncabezado= encabezadoTablas(select_query,conexion)
         # Obtener los nombres de las columnas
        columnas = [column[0] for column in nameEncabezado]

         # Determinar el ancho máximo de cada columna
        col_widths = [len(col) for col in columnas]
        for fila in filas:
            for i, cell in enumerate(fila):
                col_widths[i] = max(col_widths[i], len(str(cell)))
        
        # Formatear la fila de encabezado
        encabezado = " | ".join(f"{col:<{col_widths[i]}}" for i, col in enumerate(columnas))
        separator = "-+-".join("-" * col_widths[i] for i in range(len(columnas)))

        print(encabezado)
        print(separator)

         # Imprimir las filas de datos
        for fila in filas:
            formatoFila = " | ".join(f"{str(cell):<{col_widths[i]}}" for i, cell in enumerate(fila))
            print(formatoFila)
  
    except:
        print('Error en leer la tabla, verifique si coloco correctamente el nombre de la tabla')

def alterTable(cur):
    # cur = encederConexion();
    try:
        print('Selecciona la tabla a alterar')
        viewTables(cur)
        table_name = input('--->')
        print(f'Se selecciono la tabla {table_name}')
        
        print('¿Que desea alterar de la tabla?')
        print('1)Agregar Columna\n2)Quitar Columna')
        alter = int(input('--->'))
        match(alter):
            case 1:
                print('Ingresa el nombre de la nueva columna')
                nameColumn = input('--->')
                print('Ingresa el tipo de dato de la nueva columna')
                typeColumn = input('--->')
                addColumn(cur, table_name, nameColumn, typeColumn)
                print('Se agrego una nueva columna')
            case 2:
                print('Ingresa el nombre de la columna a eliminar')
                nameColumn = input('--->')
                dropColumn(cur, table_name, nameColumn)
                print(f'Se elimino la columna {nameColumn}')
            case _:
                print('Dato ingresado no valido')
        
    except :
        print('No se ingresaron los valores correctamente')
          

def dropTableFunction(cur):
    # cur = encederConexion();
    try:
        print('Se ha seleccionado el comando DROP TABLE, esto eliminara la tabla')
        print('Esta operacion no se puede deshacer, ¿desea continuar?')
        print('1)Si\n2)No')
        alter = int(input('--->'))
        match(alter):
            case 1:
                print('Ingresa el nombre de la tabla a eliminar')
                viewTables(cur)
                nameTable = input('--->')
                print(f'Se selecciono la tabla {nameTable}')
                dropTable(cur, nameTable)
                print('Se elimino la tabla')
            case 2:
                print('Operacion cancelada')
            case _:
                print('Dato ingresado no valido')
        


    except :
        print('No se ingresaron los valores correctamente')

def eliminarPais(idPais, conexion):
    try:
        #cur = conexion.cursor()
        #queryEliminar = "BEGIN TRAN\n"

        # Iniciar transacción
        conexion.execute("BEGIN TRAN")
        
        # Verificar que el país exista
        query_pais = f"SELECT * FROM paises WHERE idPais = {idPais}"
        pais = impactarDB(query_pais, conexion, 'consultas')
        if not pais:
            raise Exception("El país no existe.")
        
        # Obtener ciudades relacionadas con el país
        query_ciudades = f"SELECT idCiudad FROM ciudades WHERE idPais = {idPais}"
        ciudades = impactarDB(query_ciudades, conexion, 'consultas')
        ciudades_id = [ciudad[0] for ciudad in ciudades]
        
        # Obtener zoológicos relacionados con las ciudades
        if ciudades_id:
            ciudades_id_str = ', '.join(map(str, ciudades_id))
            query_zoologicos = f"SELECT idZoo FROM zoologicos WHERE idCiudad IN ({ciudades_id_str})"
            zoologicos = impactarDB(query_zoologicos, conexion, 'consultas')
            zoologicos_id = [zoo[0] for zoo in zoologicos]
            
            # Manda advertencias para los zoológicos relacionados
            if zoologicos_id:
                continuar = True
                while(continuar):
                    opcionEliminar= int(input("Seleccionar 1 si quiere eliminar los zoologicos relacionados al pais(ciudad), 2 para regresar al ménu principal: "))
                    match(opcionEliminar):
                        case 1:
                            zoologicos_ids_str = ', '.join(map(str, zoologicos_id))
                            query_delete_zoologicos = f"DELETE FROM zoologicos WHERE idZoo IN ({zoologicos_ids_str})"
                            impactarDB(query_delete_zoologicos, conexion)
                            continuar =False
                        case 2: 
                            continuar =False
                            raise Exception("Deber modificar los datos zoologico desde el menu principal para poder eliminar el pais")
                        case _:
                            print("Valor ingresado no valido")                       
            # Eliminar ciudades relacionadas
            query_delete_ciudades = f"DELETE FROM ciudades WHERE idCiudad IN ({ciudades_id_str})"
            impactarDB(query_delete_ciudades, conexion)
        
        # Obtener información de animales relacionada con el país
        query_informacion_animales = f"SELECT numIdentificacion FROM informacionAnimales WHERE idPais = {idPais}"
        informacion_animales = impactarDB(query_informacion_animales, conexion, 'consultas')
        informacion_animales_id = [info[0] for info in informacion_animales]

        # Eliminar especieAnimales relacionados con informacionAnimales
        if informacion_animales_id:
            informacion_animales_ids_str = ', '.join(map(str, informacion_animales_id))
            query_delete_especie_animales = f"DELETE FROM especieAnimales WHERE idInformacionEspecie IN ({informacion_animales_ids_str})"
            impactarDB(query_delete_especie_animales, conexion)
        
        # Eliminar información de animales relacionada con el país
        query_delete_informacion_animales = f"DELETE FROM informacionAnimales WHERE idPais = {idPais}"
        impactarDB(query_delete_informacion_animales, conexion)  

        # Eliminar el país
        query_delete_pais = f"DELETE FROM paises WHERE idPais = {idPais}"
        impactarDB(query_delete_pais, conexion)
        
        # Confirmar la transacción
        conexion.commit()
        print("El país y las filas relacionadas se han eliminado correctamente.")
    
    except Exception as e:
        conexion.rollback()
        print("Error en la transacción, cambios revertidos:", e)
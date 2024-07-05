import conexionDB as cbd 
""" Importamos del archivo que hacemos nuestra conexion como cbd = conexion base de datos """

""" Variables globales """


def encederConexion():
    conexion = cbd.iniciarConexion() #Decimos que conexion es igual al objeto de la conexion para instanciarlo
    cur = conexion.cursor() #Crearemos un cursor que nos permite manipular nuestra base de datos
    return cur

def apagarConexion(cur):
    cur.close()

""" Universal para todo el crud, una vez teniendo el query se llama esta funcion """
def impactarDB(query, cur, accion):
    cur.execute(query)  #Mandar la consulta
    if accion == 'consultas' :
        consulta = cur.fetchall() #Ejecutar la consulta para leer y trael lo que consigue (Aqui hacemos el READ)

        return consulta
    cur.commit() #Ejecutar la consulta
    cur = apagarConexion(cur)


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

def informacionCiudades():
    cur = encederConexion() #Traemos el cursos para hacer modficaciones en la base de datos
    query = 'SELECT * FROM ciudades'
    print(impactarDB(query,cur, 'consultas'))
    exit



""" Pedir datos al usuario """
def crearTabla():
    """ Encedemos la conexion con la base de datos """
    cur = encederConexion() #Traemos el cursos para hacer modficaciones en la base de datos
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

def crearZoo():
    try:
        idZoo = input('Ingresa el Id del Zoo --->')
        nombre = input('Ingresa en nombre del Zoo --->')
        tamanio = float(input('Ingresa el tamanio del zoologico --->'))
        presupuesto = float(input('Ingresa el presupuesto--->'))
    except :
        print('No se ingresaron los valores correctamente')


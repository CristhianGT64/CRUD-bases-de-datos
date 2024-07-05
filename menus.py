import conexionDB as cbd 
""" Importamos del archivo que hacemos nuestra conexion como cbd = conexion base de datos """

""" Variables globales """

conexion = cbd.iniciarConexion() #Decimos que conexion es igual al objeto de la conexion para instanciarlo
cur = conexion.cursor() #Crearemos un cursor que nos permite manipular nuestra base de datos

""" Prueba de creacion de una tabla """
sql = "CREATE TABLE prueba2 ( "
sql += "idPrueba INTEGER PRIMARY KEY, "
sql += "nombre1 VARCHAR(255),"
sql += ' );'

cur.execute(sql)  #Mandar la consulta
cur.commit() #Ejecutar la consulta


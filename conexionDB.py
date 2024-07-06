""" Primero que debe de cargar """

import pyodbc
server = 'DESKTOP-72I1FFA\SQLEXPRESS'
database = 'zoo'
username = 'python'
password = 'root'

""" Creamos una conexion con la base de datos utilizando los controladores"""
cadenaConexion = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};Encrypt=YES;TrustServerCertificate=yes;'


def conexionDB(cadenaConexion):
    try:
        """ Intentamos que se realice la conexion con la base de datos almacenando la conexion 
         en la variable de conexion """
        conexion = pyodbc.connect(cadenaConexion)
        return conexion #Retornamos la conexion con la base de datos
    except pyodbc.Error as error:
        print('Error al conectarse a la base de datos presentado por: ', error )

def iniciarConexion():
    return conexionDB(cadenaConexion) #Retornamos el objeto de la base de datos

# iniciarConexio()


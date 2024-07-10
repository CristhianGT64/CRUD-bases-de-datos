import crud #Importames el archivo de crud para las funciones
import conexionDB as sqlServer
import menuPrincipal as MP

continuar = True #Para salir del menu

def Login ():
    while continuar:
        try:
            print("Inicio de sesion")
            usuario = input("Ingresa tu usuario --> ")
            contrasena = input("Ingresa tu usuario --> ")

        except:
            print(" ----- Usuario o contrasenia incorrectos ")
        else:
            conexion = sqlServer.iniciarConexion('DESKTOP-72I1FFA\SQLEXPRESS', 'zoo', usuario, contrasena )
            if(conexion):
                print('Conectado correctamente a la base de datos')
                print('Bienvenido al sistema')
                MP.menuPrincipal(conexion)
            else:
                print('Error con este usuario')
                print(conexion)
""" Empezar con el login """
Login()
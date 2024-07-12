import crud

def loguiarUsuario(cur, usuario, contrasena):
    query = f"CREATE LOGIN {usuario} WITH PASSWORD = '{contrasena}';"
    crud.impactarDB(query, cur, "loguear")

def permisosLectura(cur, usuario):
    query = f'ALTER ROLE db_datareader ADD MEMBER {usuario};'
    print(query)
    crud.impactarDB(query, cur, 'Escritura')

def usuarioLogin(cur, usuario):
    query = f'CREATE USER {usuario} FOR LOGIN {usuario};'
    print(query)
    crud.impactarDB(query, cur, 'Escritura')

def crearUsuario(cur):
    try:
        print('----- Creacion de un nuevo usuario -----')
        usuario = input('Ingresa el nombre del usuario ---> ')
        contrasena = input('Ingresa una contrasenia --- > ')
        loguiarUsuario(cur, usuario, contrasena)
        #Asignar permisos de solo lectura
        usuarioLogin(cur, usuario) #Crear el usuario para ser usado
        permisosLectura(cur, usuario) #Dar permisos solo de escritura
        print('Usuario creado correctamente')
    except:
        print('Error al crear el usuario')
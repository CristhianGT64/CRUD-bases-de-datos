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

def otorgarPermisos(cur, usuario, permisos):
    for permiso in permisos:
        query = f'GRANT {permiso} TO {usuario};'
        crud.impactarDB(query, cur, 'Otorgar Permisos')

def permisosEscritura(cur, usuario):
    query = f'ALTER ROLE db_datawriter ADD MEMBER {usuario};'
    crud.impactarDB(query, cur, 'Escritura')

def permisosEjecutar(cur, usuario):
    query = f'ALTER ROLE db_executor ADD MEMBER {usuario};'
    crud.impactarDB(query, cur, 'Ejecutar Procedimientos')

def otorgarPermisosUsuario(cur):
    try:
        print('----- Otorgar permisos a un usuario -----')
        usuario = input('Ingresa el nombre del usuario ---> ')
        
        permisos = input('Ingresa los permisos a otorgar (separados por comas) ---> ').split(',')
        permisos = [permiso.strip() for permiso in permisos]  # Limpiar espacios

        otorgarPermisos(cur, usuario, permisos)  # Otorgar permisos especificados
        permisosEscritura(cur, usuario)          # Dar permisos de escritura
       
       #Esto dar error ya que no puedo modificar el rolo db_executor  porque no existe(Verficar) 
       # permisosEjecutar(cur, usuario)           # Dar permisos de ejecución

        print('Permisos otorgados correctamente')
    except Exception as e:
        print('Error al otorgar permisos:', e)


def quitarPermisosUsuario(cur):
    try:
        print('----- Quitar permisos a un usuario -----')
        usuario = input('Ingresa el nombre del usuario ---> ')
        
        permisos = input('Ingresa los permisos a quitar (separados por comas) ---> ').split(',')
        permisos = [permiso.strip() for permiso in permisos]  # Limpiar espacios

        for permiso in permisos:
            query = f'REVOKE {permiso} FROM {usuario};'
            crud.impactarDB(query, cur, 'Quitar Permisos')
        
        print('Permisos quitados correctamente')
    except Exception as e:
        print('Error al quitar permisos:', e)       
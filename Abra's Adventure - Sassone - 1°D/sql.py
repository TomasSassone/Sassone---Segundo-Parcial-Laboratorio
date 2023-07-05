import sqlite3

def crear_base():
    '''crea la base de datos, con los datos ID, nombre del jugador y su score'''
    with sqlite3.connect("database.db") as conexion:
        try:
            # query CREATE (table)
            sentencia = '''
                        create table Jugadores
                        (
                            id integer primary key autoincrement,
                            nombre text,
                            score integer
                        )
                        '''
            conexion.execute(sentencia)
            print("tabla creada con exito")
        except:
            print("Error al crear la base!")

def insertar_usuario(nombre:str, score:int):
    '''inserta un nuevo usuario en la tabla de Jugadores, junto con su score'''
    with sqlite3.connect("database.db") as conexion:
        try:
            sentencia = '''
                        insert into Jugadores(nombre, score) values(?,?)
                        '''
            conexion.execute(sentencia, (nombre, score)) #si es un solo parametro lleva una coma al final ("tomas",) o (nombre,) si es una var
            print("datos ingresados con exito")
        except:
            print("error al insertar usuario")

def obtener_datos():
    '''obtiene los datos de los mejores tres jugadores en relacion a su score y los devuelve en forma de una lista de diccionarios, donde
    cada diccionario corresponde a una fila del top 3'''
    with sqlite3.connect("database.db") as conexion:
        try:
            sentencia = '''
                        select nombre, score from Jugadores order by score desc limit 3
                        '''
            cursor = conexion.execute(sentencia)

            print("datos recibidos con exito")
            lista_filas = []
            for fila in cursor:
                nombre = fila[0]  # Accede al primer elemento de la tupla (nombre)
                score = fila[1]  # Accede al segundo elemento de la tupla (score)
                fila_dict = {'nombre': nombre, 'score': score}  # Crea un diccionario con el nombre y score
                lista_filas.append(fila_dict)  # Agrega el diccionario a la lista_filas
            return lista_filas
        except:
            print("error!!!")

def editar_score(nuevo_score: int):
    '''permite editar el score de un jugador para actualizarlo en caso de lograr un nuevo hi-score'''
    with sqlite3.connect("database.db") as conexion:
        sentencia = '''
                    UPDATE Jugadores SET score = ? WHERE id = (
                        SELECT MAX(id) FROM Jugadores
                    )
                    '''
        conexion.execute(sentencia, (nuevo_score,))
        print("datos editados con éxito!")






# with sqlite3.connect("database.db") as conexion:
#     try:
#         sentencia = '''
#                     delete from Jugadores where score < 170
#                     ''' #SIN WHERE SE BORRAN TODAS LAS CELDAS
#         cursor = conexion.execute(sentencia)

#         print("datos eliminados con exito")
#         for fila in cursor:
#             print(fila)
#     except:
#         print("error al borrar datos!")
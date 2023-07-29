from configBD.connBD import connectionBD  # Conexión a BD


def lista_albumBD():
    try:
        with connectionBD() as conexion_MySQLdb:
            with conexion_MySQLdb.cursor(dictionary=True) as cursor:
                querySQL = "SELECT * FROM album ORDER BY id_album DESC"
                cursor.execute(querySQL)
                resultadoQuery = cursor.fetchall()
        return resultadoQuery

    except Exception as e:
        print(f"Ocurrió un error, lista_albumBD: {e}")
        return []


def detalles_album(id_album):
    try:
        with connectionBD() as conexion_MySQLdb:
            with conexion_MySQLdb.cursor(dictionary=True) as cursor:
                querySQL = """
                  SELECT 
                        a.album_foto,
                        f.name_foto,
                        f.url_foto
                  FROM album AS a
                  INNER JOIN fotos AS f
                      ON a.id_album = f.id_album
                  WHERE a.id_album = %s
                """
                params = (id_album,)
                cursor.execute(querySQL, params)
                fotos_album = cursor.fetchall()
        return fotos_album

    except Exception as e:
        print(f"Ocurrió un error, detalles_album: {e}")
        return []

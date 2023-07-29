
import os
# Para subir archivo tipo foto al servidor
from werkzeug.utils import secure_filename
import uuid  # Modulo de python para crear un string
from os import path  # Modulo para obtener la ruta o directorio


from configBD.connBD import connectionBD  # Conexión a BD


def procesar_formulario(album_foto, files):
    # Registrando el Album
    result_process_album = guardar_AlbumBD(album_foto)
    if result_process_album:
        # Registrando las fotos del Album
        misFiles = procesarFotos(files, result_process_album)
        if (misFiles != False):
            # Registrando todas las foton en BD
            resultData = guardar_fotosBD(misFiles, result_process_album)
            return resultData or 0


# Guardar album_foto
def guardar_AlbumBD(album_foto):
    try:
        with connectionBD() as conexion_MySQLdb:
            with conexion_MySQLdb.cursor(dictionary=True) as cursor:
                SQL_Insert = "INSERT INTO album(album_foto) VALUES (%s)"
                valores = (album_foto,)
                cursor.execute(SQL_Insert, valores)
                conexion_MySQLdb.commit()

                # Capturando el ultimos id_album registrado
                ultimo_album_foto_registrado = cursor.lastrowid
        return ultimo_album_foto_registrado

    except Exception as e:
        return f'Error en la función guardar_AlbumBD: {str(e)}'

# Guardar todas las imagenes asociadas al Album registrado


def procesarFotos(files, result_process_album):
    try:
        # Definiendo un diccionario vacio
        nombres_archivos = []
        for key, file in files.items():
            if key.startswith('archivo_'):
                # Nombre original del archivo
                filename = secure_filename(file.filename)
                extension = os.path.splitext(filename)[1]

                # Creando un string de 50 caracteres
                nuevoNameFile = (uuid.uuid4().hex + uuid.uuid4().hex)[:100]

                nombreFile = nuevoNameFile + extension

                # Construir la ruta completa de subida del archivo
                basepath = os.path.abspath(os.path.dirname(__file__))
                upload_dir = os.path.join(
                    basepath, f'../static/upload_fotos/album_{result_process_album}')

                # Validar si existe la ruta y crearla si no existe
                if not os.path.exists(upload_dir):
                    os.makedirs(upload_dir)
                    # Dando permiso a la carpeta
                    os.chmod(upload_dir, 0o755)

                # Construir la ruta completa de subida del archivo
                upload_path = os.path.join(upload_dir, nombreFile)
                file.save(upload_path)

                nombres_archivos.append(nombreFile)

        # Retornando un diccionario con los nombres de cada foto recibida
        return nombres_archivos
    except Exception as e:
        print("Error al procesar archivo:", e)
        return []


# Guardando todas las fotos que llegan desde el formulario
def guardar_fotosBD(misFiles, result_process_album):
    try:
        with connectionBD() as conexion_MySQLdb:
            with conexion_MySQLdb.cursor(dictionary=True) as cursor:
                sql = "INSERT INTO fotos (id_album, name_foto, url_foto) VALUES (%s, %s, %s)"
                for filename in misFiles:
                    urlFile = f"upload_fotos/album_{result_process_album}/{filename}"
                    valores = (result_process_album, filename, urlFile)
                    cursor.execute(sql, valores)

                conexion_MySQLdb.commit()
                resultado_insert = cursor.rowcount  # Retorna 1 o 0
                return resultado_insert

    except Exception as e:
        return f'Se produjo un error en guardar_imagenesBD: {str(e)}'

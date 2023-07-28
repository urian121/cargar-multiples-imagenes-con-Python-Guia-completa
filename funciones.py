
import os

# Para subir archivo tipo foto al servidor
from werkzeug.utils import secure_filename
import uuid  # Modulo de python para crear un string

from flask import request, jsonify
from os import path  # Modulo para obtener la ruta o directorio
import datetime


from configBD.connBD import connectionBD  # Conexión a BD


def procesar_formulario(album_foto, file):
    process_album = guardar_AlbumBD(album_foto)
    if process_album:
        mes_actual = datetime.now().strftime("%B_%Y")
        misFiles = procesarFile(file, mes_actual)
        if (misFiles != False):
            resultData = guardar_fotosBD(album_foto, misFiles)
            if (resultData == 1):
                return jsonify({'status_server': 1, 'mensaje': 'La consignación fue registrada con correctamente.', 'status_mensaje': 'success'})
            else:
                return jsonify({'status_server': 0, 'mensaje': 'Ocurrio un error en el registro', 'status_mensaje': 'error'})
        else:
            return jsonify({'status_server': 0, 'mensaje': 'El archivo supera el peso establecido, recuerda maximo 8 MB', 'status_mensaje': 'error'})


def procesarFile(files, mes_actual):
    try:
        nombres_archivos = []
        for key, file in files.items():
            if key.startswith('archivo_'):
                # Nombre original del archivo
                filename = secure_filename(file.filename)
                extension = os.path.splitext(filename)[1]

                # Creando un string de 100 caracteres
                nuevoNameFile = (uuid.uuid4().hex + uuid.uuid4().hex +
                                 uuid.uuid4().hex + uuid.uuid4().hex)[:100]

                nombreFile = nuevoNameFile + extension

                # Construir la ruta completa de subida del archivo
                basepath = os.path.abspath(os.path.dirname(__file__))
                upload_dir = os.path.join(
                    basepath, f'../static/upload_fotos/{mes_actual}')

                # Validar si existe la ruta y crearla si no existe
                if not os.path.exists(upload_dir):
                    os.makedirs(upload_dir)
                    # Dando permiso a la carpeta
                    os.chmod(upload_dir, 0o755)

                # Construir la ruta completa de subida del archivo
                upload_path = os.path.join(upload_dir, nombreFile)
                file.save(upload_path)

                nombres_archivos.append(nombreFile)

        return nombres_archivos
    except Exception as e:
        print("Error al procesar archivo:", e)
        return []


# Guardar Album
def guardar_AlbumBD(album):
    try:
        with connectionBD() as conexion_MySQLdb:
            with conexion_MySQLdb.cursor(dictionary=True) as cursor:
                SQL_Insert = (
                    "INSERT INTO album(album) VALUES (%s,)")
                valores = (album,)
                cursor.execute(SQL_Insert, valores)
                conexion_MySQLdb.commit()
                resultado_insert = cursor.rowcount
        return resultado_insert

    except Exception as e:
        return f'Se produjo un error en guardar_AlbumBD: {str(e)}'


# Insertando todas las imagenes que llegan
def guardar_fotosBD(ultimo_id_consignacion, misFiles, code_tienda, mes_actual):
    try:
        with connectionBD() as conexion_MySQLdb:
            with conexion_MySQLdb.cursor(dictionary=True) as cursor:
                sql = "INSERT INTO fotos (album, name_foto, url_foto) VALUES (%s, %s, %s)"
                for filename in misFiles:
                    urlFile = f"upload_fotos/{mes_actual}/{filename}"
                    valores = (ultimo_id_consignacion, filename, urlFile)
                    cursor.execute(sql, valores)

                conexion_MySQLdb.commit()
                resultado_insert = cursor.rowcount
                return resultado_insert

    except Exception as e:
        return f'Se produjo un error en guardar_imagenesBD: {str(e)}'

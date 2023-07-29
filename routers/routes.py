# Instanciam¿ndo mi aplicación
from app import app
# Importando de la clase flask algunos paquetes
from flask import render_template, request, redirect, url_for, jsonify

# Importando todas mis funciones
from funciones.funciones import *
from funciones.fotos_album import *


# Definiendo un decorador
@app.route('/')
# Definiendo una función llamada inicio
def inicio():
    # Retornando una vista sin parametros
    return render_template('index.html')


@app.route('/procesar-formulario-album', methods=['POST'])
def processForm():
    # print(f"Data request: {request.form}")
    album_foto = request.form['album_foto']
    if request.files:
        file = request.files
        resultado = procesar_formulario(album_foto, file)
        if (resultado == 1):
            return jsonify({'status_server': 1, 'mensaje': 'El Album fue creado correctamente.', 'status_mensaje': 'success'})
        else:
            return jsonify({'status_server': 0, 'mensaje': 'Ocurrio un error al crear el Album', 'status_mensaje': 'error'})


@app.route('/lista-de-album', methods=['GET'])
def lista_album():
    return render_template('lista_album.html', lista_album=lista_albumBD())


# Ver fotos del Album seleccionado
@app.route('/ver-album/<string:id_album>', methods=['GET'])
def verAlbunBD(id_album):
    return render_template('fotos_album.html', fotos_album=detalles_album(id_album))


@app.errorhandler(404)
def not_found(error):
    return redirect(url_for('inicio'))


@app.errorhandler(500)
def server_error(error):
    return redirect(url_for('inicio'))

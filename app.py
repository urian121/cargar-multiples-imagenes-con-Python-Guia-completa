# Importando la clase Flask de flask y algunos paquetes.
from flask import Flask, redirect, render_template, url_for
from funciones import *

# Declarando nombre de la aplicación e inicializando,
# crear la aplicación Flask
# Creamos una app instanciando la clase Flask (automáticamente el nombre de la app)
app = Flask(__name__)
application = app
app.secret_key = '97110c78ae51a45af397be6534caef90ebb9b1dcb3380af008f90b23a5d1616bf19bc29098105da20fe'


# Definiendo un decorador
@app.route('/')
# Definiendo una función llamada inicio
def inicio():
    # Retornando una vista sin parametros
    return render_template('index.html')


@app.route('/procesar-formulario', methods=['POST'])
def processForm():
    # print(f"Data request: {request.form}")
    album_foto = request.form['album_foto']
    if request.files:
        file = request.files
        resultado = procesar_formulario(album_foto, file)


@app.errorhandler(404)
def not_found(error):
    return redirect(url_for('inicio'))


@app.errorhandler(500)
def server_error(error):
    return redirect(url_for('inicio'))


# Ejecutando el objeto Flask
# Condicional de que si la aplicación ejecutada se coincide al nombre de la aplicación
if __name__ == '__main__':
    # Método que indica la app, con la dirección, puerto y mode de argumento(debug)
    app.run(debug=True, port=5600)

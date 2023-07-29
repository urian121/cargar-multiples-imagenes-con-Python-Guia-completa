
# Declarando nombre de la aplicación e inicializando, crear la aplicación Flask
from app import app

from routers.routes import *


# Ejecutando el objeto Flask
# Condicional de que si la aplicación ejecutada se coincide al nombre de la aplicación
if __name__ == '__main__':
    # Método que indica la app, con la dirección, puerto y mode de argumento(debug)
    app.run(debug=True, port=5400)

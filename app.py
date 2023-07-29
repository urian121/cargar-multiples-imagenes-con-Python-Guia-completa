# Importando la clase Flask de flask y algunos paquetes.
from flask import Flask

# Declarando nombre de la aplicación e inicializando,
# crear la aplicación Flask
# Creamos una app instanciando la clase Flask (automáticamente el nombre de la app)
app = Flask(__name__)
application = app
app.secret_key = '97110c78ae51a45af3e6534caef90ebb9b1dcb3380af008f90b23a5d1616bf19bc29098105da20fe'

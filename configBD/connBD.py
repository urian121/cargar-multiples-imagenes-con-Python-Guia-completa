

# Importando Libreria mysql.connector para conectar Python con MySQL
import mysql.connector
from mysql.connector.errors import Error


def connectionBD():
    try:
        # connection = mysql.connector.connect(
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="bd_album",
        )
        if connection.is_connected():
            # print("Conexión exitosa a la BD")
            return connection

    except mysql.connector.Error as error:
        print(f"No se pudo conectar: {error}")

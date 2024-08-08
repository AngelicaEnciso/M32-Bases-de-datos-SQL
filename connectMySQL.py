import mysql.connector
from mysql.connector import Error


def connect_to_mysql():
    try:
        # Establecer la conexión con la base de datos
        connection = mysql.connector.connect(
            host='195.179.238.58',  # por ejemplo, 'localhost'
            database='u927419088_testing_sql',
            user='u927419088_admin',
            password='#Admin12345#'
        )

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Conectado a MySQL Server versión ", db_Info)
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            print("Conectado a la base de datos ", record)

    except Error as e:
        print("Error al conectar con MySQL", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión a MySQL cerrada")


# Llamar a la función para conectarse a la base de datos
connect_to_mysql()

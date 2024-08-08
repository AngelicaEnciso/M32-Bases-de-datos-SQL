import mysql.connector
from mysql.connector import Error
import pandas as pd


def export_curso_to_excel():
    try:
        # Establecer la conexión con la base de datos
        connection = mysql.connector.connect(
            host='195.179.238.58',  # por ejemplo, 'localhost'
            database='u927419088_testing_sql',
            user='u927419088_admin',
            password='#Admin12345#'
        )


        if connection.is_connected():
            print("Conectado a la base de datos")
            cursor = connection.cursor()

            #creando registro
            registro = [50, 'Estructura de Datos', 104]

            # Ejecutar la consulta para obtener los registros de la tabla curso
            query = "INSERT INTO curso (idCurso, nombreDescriptivo, nAsignaturas) VALUES (%s,%s,%s)"
            cursor.execute(query,registro)

            connection.commit()

            print("El Registro insertado CORRECTAMENTE")

    except Error as e:
        print("Error al conectar con MySQL", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión a MySQL cerrada")


# Llamar a la función para exportar los datos
export_curso_to_excel()

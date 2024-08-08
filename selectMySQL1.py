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

            # Ejecutar la consulta para obtener los registros de la tabla curso
            query = "SELECT * FROM curso"
            cursor.execute(query)

            # Obtener los nombres de las columnas
            columns = [col[0] for col in cursor.description]

            # Convertir los registros en un DataFrame
            records = cursor.fetchall()
            df = pd.DataFrame(records, columns=columns)

            print (df['nombreDescriptivo'])


            # Exportar el DataFrame a un archivo Excel
            df.to_excel("curso_exportado.xlsx", index=False)
            print("Los datos han sido exportados exitosamente a 'curso_exportado.xlsx'")

    except Error as e:
        print("Error al conectar con MySQL", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión a MySQL cerrada")


# Llamar a la función para exportar los datos
export_curso_to_excel()

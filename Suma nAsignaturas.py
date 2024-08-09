import psycopg2

# Configuración de la conexión
conn = psycopg2.connect(
    host='195.179.238.58',
    database='u927419088_testing_sql',
    user='u927419088_admin',
    password='#Admin12345#'
)

# Crear un cursor para interactuar con la base de datos
cur = conn.cursor()

# Consulta para sumar los créditos
cur.execute("SELECT SUM(nAsignaturas) AS total_nAsignaturas FROM cursos;")
total_nAsignaturas = cur.fetchone()[0]  # Obtener el resultado

print(f"El total de créditos es: {total_nAsignaturas}")

# Cerrar el cursor y la conexión
cur.close()
conn.close()

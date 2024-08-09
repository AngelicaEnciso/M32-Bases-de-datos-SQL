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

# Consulta para actualizar el registro
cur.execute("""
    UPDATE cursos
    SET nombreDescriptivo = %s
    WHERE idCurso = %s;
    """,
    ('Gestión de Proyectos de Software', 50)
)

# Confirmar los cambios en la base de datos
conn.commit()

print("Registro actualizado correctamente.")

# Cerrar el cursor y la conexión
cur.close()
conn.close()

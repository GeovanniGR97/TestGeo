import sqlite3

def fetch_data_in_chunks(query, db_name, chunk_size=1000):
    # Conectar a la base de datos
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Ejecutar la consulta
    cursor.execute(query)

    # Recuperar datos en lotes (chunks)
    while True:
        rows = cursor.fetchmany(chunk_size)  # Obtener un número determinado de filas
        if not rows:
            break  # Si no hay más filas, termina el bucle
        for row in rows:
            yield row  # Devuelve una fila por vez

    # Cerrar la conexión
    cursor.close()
    conn.close()

# Usando el generador para procesar los datos
for fila in fetch_data_in_chunks("SELECT * FROM mi_tabla", "mi_base_de_datos.db"):
    print(fila)
#############################################################################################
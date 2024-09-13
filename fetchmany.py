import mysql.connector

def fetch_data_in_chunks(query, db_config, chunk_size=1000):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute(query)
    
    while True:
        rows = cursor.fetchmany(chunk_size)
        if not rows:
            break
        for row in rows:
            yield row

    cursor.close()
    conn.close()

# Configuración de la base de datos
db_config = {
    'user': 'tu_usuario',
    'password': 'tu_contraseña',
    'host': 'localhost',
    'database': 'mi_base_de_datos'
}

for fila in fetch_data_in_chunks("SELECT * FROM mi_tabla", db_config):
    print(fila)

def procesar_estadisticas(query, db_name):
    total = 0
    suma = 0
'''
    for fila in fetch_data_in_chunks(query, db_name):
        valor = fila[1]  # Por ejemplo, segundo campo
        total += 1
        suma += valor
    
    print(f"Total de registros procesados: {total}")
    print(f"Suma total de valores: {suma}")

procesar_estadisticas("SELECT id, valor FROM tabla_grande", "mi_base_de_datos.db")
'''
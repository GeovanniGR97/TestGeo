def mostrar_linea(num, linea):
    print(num, "x", linea, "=", num * linea)

for numero in range(1, 11):  # Desde la tabla del 1 hasta la del 10
    print(f"\nTabla del {numero}:")  # Encabezado para cada tabla
    for n in range(1, 11):  # Del 1 al 10 en cada tabla
        mostrar_linea(numero, n)

import mysql.connector

# Conexión a la base de datos
def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",       
        password="", 
        database="inventario"
    )

# Insertar un nuevo producto
def insertar_producto(nombre, cantidad, precio):
    conexion = conectar_bd()
    cursor = conexion.cursor()
    query = "INSERT INTO productos (nombre, cantidad, precio) VALUES (%s, %s, %s)"
    valores = (nombre, cantidad, precio)
    cursor.execute(query, valores)
    conexion.commit()
    print("Producto insertado con éxito.")
    conexion.close()

# Actualizar la cantidad de un producto
def actualizar_producto(producto_id, nueva_cantidad):
    conexion = conectar_bd()
    cursor = conexion.cursor()
    query = "UPDATE productos SET cantidad = %s WHERE id = %s"
    valores = (nueva_cantidad, producto_id)
    cursor.execute(query, valores)
    conexion.commit()
    if cursor.rowcount > 0:
        print("Producto actualizado con éxito.")
    else:
        print("No se encontró un producto con ese ID.")
    conexion.close()

# Mostrar todos los productos
def listar_productos():
    conexion = conectar_bd()
    cursor = conexion.cursor()
    query = "SELECT * FROM productos"
    cursor.execute(query)
    resultados = cursor.fetchall()
    print("\nID | Nombre | Cantidad | Precio")
    print("-" * 30)
    for producto in resultados:
        print(f"{producto[0]} | {producto[1]} | {producto[2]} | ${producto[3]:.2f}")
    conexion.close()

# Calcular el valor total del inventario
def calcular_valor_total():
    conexion = conectar_bd()
    cursor = conexion.cursor()
    query = "SELECT SUM(cantidad * precio) AS valor_total FROM productos"
    cursor.execute(query)
    resultado = cursor.fetchone()
    valor_total = resultado[0] if resultado[0] else 0
    print(f"\nEl valor total del inventario es: ${valor_total:.2f}")
    conexion.close()

# Menú principal
if __name__ == "__main__":
    while True:
        print("\nGestión de Inventarios")
        print("1. Insertar producto")
        print("2. Actualizar cantidad de un producto")
        print("3. Listar productos")
        print("4. Calcular valor total del inventario")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            insertar_producto(nombre, cantidad, precio)
        elif opcion == "2":
            producto_id = int(input("ID del producto a actualizar: "))
            nueva_cantidad = int(input("Nueva cantidad: "))
            actualizar_producto(producto_id, nueva_cantidad)
        elif opcion == "3":
            listar_productos()
        elif opcion == "4":
            calcular_valor_total()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

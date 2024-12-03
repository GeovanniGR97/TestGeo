import mysql.connector

# Conexión a la base de datos
def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",       # Cambia esto
        password="", # Cambia esto
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

# Mostrar todos los productos
def listar_productos():
    conexion = conectar_bd()
    cursor = conexion.cursor()
    query = "SELECT * FROM productos"
    cursor.execute(query)
    resultados = cursor.fetchall()
    for producto in resultados:
        print(producto)
    conexion.close()

# Ejemplo de uso
if __name__ == "__main__":
    while True:
        print("\nGestión de Inventarios")
        print("1. Insertar producto")
        print("2. Listar productos")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            insertar_producto(nombre, cantidad, precio)
        elif opcion == "2":
            listar_productos()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

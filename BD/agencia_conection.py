import mysql.connector

def conectar_bd():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password="",
        database = "agencia"
    )

#Inserccion de datos
def insertar_auto(nombre, color, cantidad, precio):
    conexion = conectar_bd()
    cursor = conexion.cursor()
    query = "INSERT INTO autos (nombre, color, cantidad, precio) VALUES (%s, %s, %s, %s)"
    valores = (nombre, color, cantidad, precio)
    cursor.execute(query, valores)
    conexion.commit()
    print("Auto agregado con exito")
    conexion.close()

# Actualización de datos 
def actualizar_auto(auto_id, nuevo_auto):
    conexion = conectar_bd()
    cursor = conexion.cursor()
    query = "UPDATE autos SET cantidad = %s WHERE id = %s"
    valores =(auto_id, nuevo_auto)
    cursor.execute = (query, valores)
    conexion.commit()
    if cursor.rowcount > 0:
        print("Producto actualizado con éxito")
    else:
        print("No se encontro un producto con ese ID")
    conexion.close

#Mostrar todos los autos
def listar_autos():
    conexion = conectar_bd()
    cursor = conexion.cursor()
    query = "SELECT * FROM autos"
    cursor.execute(query)
    resultados = cursor.fetchall()
    print("\nID | Nombre | Color | Cantidad | Precio")
    print("-" * 50)
    for auto in resultados:
        auto(f"{auto[0]} | {auto[1]} | {auto[2]} | {auto[3]} | ${auto[4]:.2f}")
    conexion.close



#Menu principal 
if __name__ == "__main__":
    while True:
        print("\nGestion de autos")
        print("1. Insertar autos")
        print("5. Salir")

        opcion = input("Selecciona una opcion: ")
        
        if opcion == "1":
            nombre = input("Nombre del auto: ")
            color = input("Color: ")
            cantidad = int(input("Cantidad: "))
            precio = int(input("Precio: "))
            insertar_auto(nombre, color, cantidad, precio)
        elif opcion == "5":
            print("Saliendo del programa")
            break
        else:
            print("Opcion no valida.....")




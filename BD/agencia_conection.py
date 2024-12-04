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




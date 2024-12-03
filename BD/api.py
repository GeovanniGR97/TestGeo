from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Conexión a la base de datos
def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",       # Cambia esto
        password="", # Cambia esto
        database="inventario"
    )

@app.route('/')
def home():
    return "¡Bienvenido a la API de Gestión de Inventarios!"




# Ruta para insertar un producto
@app.route('/productos', methods=['POST'])
def insertar_producto():
    data = request.json
    nombre = data.get("nombre")
    cantidad = data.get("cantidad")
    precio = data.get("precio")

    conexion = conectar_bd()
    cursor = conexion.cursor()
    query = "INSERT INTO productos (nombre, cantidad, precio) VALUES (%s, %s, %s)"
    valores = (nombre, cantidad, precio)
    cursor.execute(query, valores)
    conexion.commit()
    producto_id = cursor.lastrowid
    conexion.close()

    return jsonify({"mensaje": "Producto insertado con éxito", "id": producto_id}), 201

# Ruta para listar todos los productos
@app.route('/productos', methods=['GET'])
def listar_productos():
    conexion = conectar_bd()
    cursor = conexion.cursor()
    query = "SELECT * FROM productos"
    cursor.execute(query)
    resultados = cursor.fetchall()
    conexion.close()

    productos = [{"id": p[0], "nombre": p[1], "cantidad": p[2], "precio": p[3]} for p in resultados]
    return jsonify(productos)

# Ruta para actualizar la cantidad de un producto
@app.route('/productos/<int:producto_id>', methods=['PUT'])
def actualizar_producto(producto_id):
    data = request.json
    nueva_cantidad = data.get("cantidad")

    conexion = conectar_bd()
    cursor = conexion.cursor()
    query = "UPDATE productos SET cantidad = %s WHERE id = %s"
    valores = (nueva_cantidad, producto_id)
    cursor.execute(query, valores)
    conexion.commit()
    conexion.close()

    if cursor.rowcount > 0:
        return jsonify({"mensaje": "Producto actualizado con éxito"})
    else:
        return jsonify({"mensaje": "Producto no encontrado"}), 404

# Ruta para calcular el valor total del inventario
@app.route('/productos/valor-total', methods=['GET'])
def calcular_valor_total():
    conexion = conectar_bd()
    cursor = conexion.cursor()
    query = "SELECT SUM(cantidad * precio) AS valor_total FROM productos"
    cursor.execute(query)
    resultado = cursor.fetchone()
    valor_total = resultado[0] if resultado[0] else 0
    conexion.close()

    return jsonify({"valor_total": valor_total})

# Iniciar servidor
if __name__ == '__main__':
    app.run(debug=True)

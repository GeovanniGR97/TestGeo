def puntuaciones(calificaciones):
    suma = sum(calificaciones)  # Sumar todas las calificaciones
    return suma / len(calificaciones)  # Calcular el promedio

calificaciones = []  # Lista vacía para almacenar las calificaciones

# Usamos un ciclo for para solicitar 3 calificaciones
for i in range(3):
    calificacion = int(input(f"Ingresa la calificación {i + 1}: "))
    calificaciones.append(calificacion)  # Agregamos la calificación a la lista

# Calculamos y mostramos el promedio
promedio = puntuaciones(calificaciones)
print(f"El promedio de las tres calificaciones es: {promedio}")


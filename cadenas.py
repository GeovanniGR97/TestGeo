texto = "Bienvenido José Geovanni"
print(texto.upper())
print(texto.lower())
print(texto.title()) #Convierte una cadena a un formato de titulo
print(texto.find("os")) #Posición donde encuentra la cadena o porición 
print(texto.count("e")) #Cantidad de ocurrencias de una letra o porción 

textoFinal = texto.replace("i", "1")
print(textoFinal)

valor = texto.isnumeric()  #Muestra true and false dependiendo si es un numero 
print(valor)

cadena_separada = texto.split(" ")
print(cadena_separada)
''' Estructura de datos que nos permiten almacenar distintos valores 
equivalentes a los arrays en otros lenguajes de programación  
estructuras dinamicas las cuales si son mutables '''

listaUno = [2, "Jose", "Geovanni", 5, 6, 7, 8, "RDZ"]
print(listaUno)
print(listaUno[:]) #Al ingresar los [:] se mostrara toda la lista
print(listaUno[3]) #Muestra que elemento deseamos ver
print(listaUno[-2]) #Muestre el elemento final 
print(listaUno[0:3])

listaUno.append("Inserccion de la lista dinamica con append")
print(listaUno)

listaUno.extend(["IDGS", 9, 10, 11])
print(listaUno)
print(listaUno.index("IDGS"))

listaUno.remove(11)
print(listaUno)

listaUno.pop()  #Elimina el ultimo elemento de la lista 
print(listaUno)



pares = []
for i in range(10):
    if i % 2 == 0: #
        pares.append(i)
print(pares)  # Output: [0, 2, 4, 6, 8]

mi_lista = []
for i in range(5):
    mi_lista.append(i)
print(mi_lista)  # Output: [0, 1, 2, 3, 4]




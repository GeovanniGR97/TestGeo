#Una tupla es una estructura de datos propia de python que permite almacenar distintos valores
#Son inmutables: no cambian una vez inicializadas

tupla = ("hola", 5, 6, "True", 555)
tuplaTest = (1,"hola", "Geo", 15,2,5,5)
print(tupla)
print(tupla[4])
print(tupla[0:3])
print(tupla[-1])

tuplaFinal = tupla + tuplaTest
print(tuplaFinal)
print(tuplaFinal.count(5))
print(tuplaFinal.count("hola"))



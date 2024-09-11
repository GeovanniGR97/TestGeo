'''
Permite extraer valores de una función y almacenarlo de uno en uno en objetos iterables
que se pueden recorrer sin la necesidad de almacenar todos a la vez en la memoria ram

def generaMultiplos7(limite):
    numero = 1
    listaNumeros = []
    while numero <= limite:
        listaNumeros.append(numero * 7)
        numero = numero + 1
    return listaNumeros #Retorna toda la lista creada
print(generaMultiplos7(10))

Cuando indicamos un * adelante de los parametros de una función, estamos indicando que se va
a recibir un número indeterminado de parametros, ademas esos parametros se recibiran e forma de tupla

'''
def devuelveLenguajes(*lenguajes):
    for leng in lenguajes:
        for letra in leng:
            yield letra
lenguajesObtenidos = devuelveLenguajes("Python", "Java", "JavaScript", "Php")
print(next(lenguajesObtenidos))


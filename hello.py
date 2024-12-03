'''def saludo():
    print("Hola geo")
saludo()

a = b = c = "Hola mundo"
print(a,b,c)

def firstFunction():
    x= "fantasic"
    print("Python is " + x)
firstFunction()

def saludo():
    print("Holaaa")
saludo()

def salidaDato():
    return "Hola con return"
mensaje = salidaDato()
print(mensaje)

def saludo():
    return "Hi"
# Para mostrar el saludo, usamos print cuando llamamos a la función
mensaje = saludo()
print(mensaje)

#PARA LA CONCATENACION ES MUCHO MEJOR USAR (+) PARA QUE SE VISUALICE MEJOR USAR UN (,) PUEDE CAUSAR UNA CONFUNCION
def concatenacionDatos():
    x = "Geovanni"
    print("Hola mi nombre es: " + x)
concatenacionDatos()

def concatenacionDatos():
    x = "Geovanni"
    print("Hola mi nombre es: " + x)
concatenacionDatos()


def saludar():
    print("Holaaaa")
saludar()

def functionReturn():
    return "Salida de la función return"
mensaje = functionReturn()
print(mensaje)

def funcionConcatenacion():
    z = "Geo"
    print("Hi my name is: " + z)
funcionConcatenacion()

def saludo():
    print ("HolaOne")
saludo()

def funcionReturn():
    return "Hola"
mensaje = funcionReturn()
print (mensaje)

def funcionConcatenacion():
    x = "GEO"
    print("Hola mi nombre es: " + x)
funcionConcatenacion()

list = ['a','j','w']
print(max(list))

list = ['a', 'd', 'x']
print(min(list))


a = 10
b = 2
print(divmod(a/b))

'''


'''
Explicación del código:
divmod(a, b): Esta función toma dos argumentos, a y b, y devuelve una tupla con dos valores:
El cociente de la división entera de a entre b.
El residuo o resto de la división de a entre b.
En este ejemplo:

divmod(17, 5) devuelve la tupla (3, 2):
Cociente: Al dividir 17 entre 5, el cociente es 3 (porque 5 * 3 = 15).
Residuo: El residuo es 2, porque 17 - 15 = 2.
Posteriormente, esos dos valores se asignan a las variables cociente y residuo, y se imprimen.

Este tipo de función es útil cuando necesitas tanto el cociente como el residuo de una división en una sola operación.
'''
'''

cociente, residuo = divmod(17,5)
print(f"Cociente: {cociente}")
print(f"Reciduo : {residuo}")


dataLen = ['jsjjs']
print(len(dataLen))

dataName = "Jose"
print(len(dataName))

dataConjuntos = ['j', 56, 'k', 'l']
print(len(dataConjuntos))

datoNumeroUno = int(input("Ingresa el primer numero: "))
datoNumeroDos = int(input("Ingresa el segundo numero: "))
if datoNumeroUno > datoNumeroDos:
    print(f"El numero {datoNumeroUno} es mayor")
elif datoNumeroUno < datoNumeroDos:
    print(f"El numero {datoNumeroDos} es mayor")
else:
    print(f"El numero {datoNumeroUno} y {datoNumeroDos} son iguales..")
    
datoPrimario = int(input("Ingresa el dato de la tabla que deseas visualizar: "))
for i in range(1,11):
    resultado = datoPrimario * i
    print(f"{datoPrimario} * {i} = {resultado}")
    

'''



c, r = divmod(17,5)
print(f"cociente: {c}")
print(f"residuo:{r}")


def salidaDato():
    return "Hola con return"
mensaje = salidaDato()
print(mensaje)
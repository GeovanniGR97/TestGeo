'''
Estructura repetitiva que nos permite realizar multiples iteraciones
basandonos en el resultado de una expresión lógica que puede tener 
como resultado un valor True and False 
'''
'''

inicio = 2 
while inicio <= 100:
    print(f"Numero par: {inicio}")
    inicio += 2
print("Termino el ciclo.........")

lista = range(1,15)
for i in lista:
    if i > 10:
        break
    print(i)

numero = 10
while numero < 5:
    if numero > 8:
        break
    print(numero)
    numero += 1
contador = 0
suma = 0
while contador < 20:
    suma = suma + contador
    contador += 1
print("La summa es :", suma)


    


    '''



indice = 1
while indice < 11:
    print(f"Valor actual: {indice}")
    indice = indice + 1
print("Termina el ciclo while...")

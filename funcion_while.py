from random import random
def generaAleatorio(cantidadNumeros):
    lista=[]
    ind=0
    while ind<cantidadNumeros:
        lista.append(random())
        ind+=1
        print(lista)
n = int(input("Introduce un valor: "))
generaAleatorio(n)        

'''
Pass: Permite continuar con una sentencia o función que ya no tiene 
un bloque de codigo......
'''
for numero in range(1, 6):
    if numero <= 3:
        pass
    else:
        print("El siguiente valor es mayor a 3..")
    print(f"El numero es: {numero}")

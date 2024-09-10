'''
Es el priducto de todos los números positivos enteros compredidos entre 1 y un uno
Factorial de 5: 1*2*3*4*5 = 120
'''
numero = int(input("Ingresa un número: "))
factorial = 1
for n in range(1, (numero + 1)):
    factorial = factorial * n
print(f"El factorial de: {numero} es de {factorial}")



#Primer ejemplo
'''
edad = int(input("Ingresa tu edad: "))

if edad > 18:
    print("Eres mayor de edad")
elif edad == 18:
    print("Tienes la edad correcta")
else:
    print("Eres menor de edad")

#Segundo ejemplo

numeroUno = int(input("Ingresa el primer numero : "))
numeroDos = int(input("Ingresa el segundo numero :"))
if numeroUno > numeroDos:
    print(f"El numero {numeroUno} es mayor que {numeroDos}")
elif numeroUno < numeroDos:
    print(f"El numero {numeroDos} es mayo que {numeroUno}")
else:
    print("Los numeros son iguales")

'''
calificacion = int(input("Ingresa tu calificación : "))
if calificacion >= 80:
    print("Pasaste la materia")
else:
    print("No pasaste")
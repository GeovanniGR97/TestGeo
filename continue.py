'''
Omite una parte del bucle cuando se cumple una condición y continua con el resto. 

'''
for numero in range(1, 6):
    if  numero == 3:
        continue
    print(f"El numero es: {numero}")
print("Bucle terminado.........")

'''
Error en tiempo de ejecucióin de un programa 

'''

numeroUno = 20
numeroDos = 2
#division = numeroUno / numeroDos
#print(f"La division entre {numeroUno} y {numeroDos} es: {division}")
#try = Se intento
try:
    resultado =  numeroUno/numeroDos
except ZeroDivisionError:
    print("No se puede dividir entre 0.....")
finally:
    print("Estudiar finally...")
print("Aqui termina mi programa......")

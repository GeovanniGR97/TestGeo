'''
Sirve para lanzar de manera intencional excepciones en python 

'''
def evaluarNota(nota):
    if nota < 0:
        raise ValueError("Valor incorrecto..")
        #raise ZeroDivisionError("No se permiten valores negativos..")
    elif nota >= 16:
        print("Excelente")
    elif nota >= 11:
        print("Aprobado")
    else:
        print("Desaprobado")
evaluarNota(-11)
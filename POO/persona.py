'''
En que consiste la programación orientada a objetos?
Trasladar la naturaleza de los objetos de la vida real a codigo de programacion
en algun lenguaje de programacion como python
-Los objetos de la realidad tienen caracteristicas (Atributos o propiedades)
y funcionalidades o comportamientos (funciones o metodos)
Ventajas:
Modularización: división en pequeñas partes de un programa completo
-Codigo fuente muy reutilizable
-Codigo fuente mas facil de incrementar en el futuro y mantener
-Si existe un fallo en una pequeña  parte del codigo el programa completo nno debe falla necesariamente
"FACIL CORREGIR LOS FALLOS"
Encapsulamiento: Ocultamiento del funcionamiento interno de un objetivo

Clase: Plantilla de un objeto de la realidad
Self = this 
'''
class persona():
    #Propiedades caracteristicas o atributos
    apellidos= ""
    nombres=  ""
    edad= 0
    despierta = False

    #Funcioalidades
    def despertar(self):
        self.despertar = True
        print("Buen día")
personaUno = persona()
personaUno.apellidos = "Gomez Rodriguez"
print(personaUno.apellidos)
personaUno.despertar()

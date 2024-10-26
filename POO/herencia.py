class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_informacion(self):
        print(f'Personna: {self.nombre} {self.apellido}, y tiene {self.edad} años')

class Alumno(Persona):
    def __init__(self, nombre, apellido, edad, nivel):
        super().__init__(nombre, apellido, edad)
        self.nivel = nivel

alumno = Alumno('Geovanni', 'Rodriguez', 26, 'Junior')
alumno.mostrar_informacion()
print(alumno.nivel)

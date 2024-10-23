class Curso():
    '''
    nombre = "Matemamaticas"
    creditos = 5
    profesion = "Ingenieria en Software"
    '''
    #Estado incial del objeto
    def __init__(self,nom,cre,pro):

        self.nombre = nom
        self.creditos = cre
        self.profesion = pro
        self.__imparticion = "Presencial" #propiedad encapsulada
    def mostrarDatos(self):
        data = f"Nombre: {self.nombre} / Creditos: {self.creditos} / Modo de impaticion: {self.__imparticion}"
        print(data)

cursoUno = Curso("Matematicas",5,"IDGS")
print(cursoUno.nombre)
cursoUno.mostrarDatos()



'''
cursoUno.imparticion = "Virtual"
print(cursoUno.imparticion)


cursoDos = Curso("EDO",6,"Meca")
print(cursoDos.nombre)
'''




#Constructores es el estado incial a nuestro objeto
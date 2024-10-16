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
        
cursoUno = Curso("Matematicas",5,"IDGS")
print(cursoUno.nombre)

cursoDos = Curso("EDO",6,"Meca")
print(cursoDos.nombre)





#Constructores es el estado incial a nuestro objeto
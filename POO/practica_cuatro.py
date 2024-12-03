from practica_dos import Pokemon

class Charmander(Pokemon):
    def __init__(self, nombre, color, nivel, voltaje_max, amperaje_max):
        super().__init__(nombre, color, nivel, voltaje_max, amperaje_max)


charmander = Charmander('Charmin','Rojito', 80, 30,50)

print(charmander.nombre, charmander.color, charmander.nivel)
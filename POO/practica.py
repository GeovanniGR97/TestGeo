class Pokemon:
    tipo = 'Electrico'
    def __init__(self, nombre, color, nivel):
        self.nombre = nombre
        self.color = color
        self.nivel = nivel

    def atacar(self):
        print(f'{self.nombre} tiene un nivel de ataque de {self.nivel/4}')

volvasor = Pokemon('Volvasor','verde',1215126)
pikachu = Pokemon('Pikachu','Amarillo', 2451515)

print(f'El pokemon {volvasor.nombre} ataca..')
volvasor.atacar()

print(f'El pokemon {pikachu.nombre} ataca..')
pikachu.atacar()



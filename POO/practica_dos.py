from practica_tres import PokemonH

class Pokemon(PokemonH):
    __tipo = 'Electrico'  # Atributo de clase
    
    def __init__(self, nombre, color, nivel, voltaje_max, amperaje_max):
        super().__init__(nombre=nombre, nivel=nivel, color=color)
        self.__voltaje_max = voltaje_max
        self.__amperaje_max = amperaje_max
        self.__nivel = nivel

    # Propiedad para acceder a `__nivel`
   

    @property
    def voltaje_max(self):
        return self.voltaje_max
    
    @voltaje_max.setter
    def voltaje_max(self, voltaje_maximo):
        if voltaje_maximo > 0 and voltaje_maximo <=100:
            self.__voltaje_max = voltaje_maximo
        else:
            print('El voltaje no puede ser mayor a 100')

    @property
    def amperaje_max(self):
        return self.amperaje_max
    
    @amperaje_max.setter
    def amperaje_max(self, amperaje_max):
        if amperaje_max > 0 and amperaje_max <=100:
            self.amperaje_max = amperaje_max
        else: print('El amperaje no puede ser mayor a 100')


    # Método para obtener el nivel (opcional)
    #def get_nivel(self):
    #   return self.__nivel

    # Método para realizar el ataque
    def atacar(self):
        print(f'{self.nombre} tiene un nivel de ataque de {self._PokemonH__nivel / 4}')

# Crear una instancia de `Pokemon`
volvasor = Pokemon('Volvasor', 'Verde', 215130, 5412351, 2630394)

# Mostrar información inicial del Pokémon
print(f'El pokemon {volvasor.nombre} tiene un nivel {volvasor.nivel}')

# Cambiar el nivel a un valor positivo (válido)
volvasor.nivel = 300000
print(f'Nuevo nivel de {volvasor.nombre}: {volvasor.nivel}')


# Intentar establecer un nivel negativo (inválido)
volvasor.nivel = 100

print(f'Nivel actual de {volvasor.nombre}: {volvasor.nivel}')

# Ejecutar el ataque para ver el nivel de ataque
volvasor.atacar()

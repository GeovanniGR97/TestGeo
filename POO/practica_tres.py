class PokemonH:
    def __init__(self, nombre, nivel, color):
        self.nombre = nombre
        self.__nivel = nivel
        self.color = color 

    @property
    def nivel(self):
        return self.__nivel

    # Setter para modificar `__nivel` con validación
    @nivel.setter
    def nivel(self, nivel):
        if nivel >= 0 and nivel <=100:
            self.__nivel = nivel
        else:
            print("El nivel no puede ser negativo.")

    
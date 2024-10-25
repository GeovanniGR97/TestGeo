class Auto:
    def __init__(self, nombre, modelo, color):
        self.nombre= nombre
        self.modelo = modelo
        self.__color = color

    def mostrar_datos(self):
        print(f'Nombre del carro: {self.nombre}')
        print(f'Marca del carro: {self.modelo}')
        print(f'Color del carro: {self.__color}')

    #get = obtener, set = asignar
    def get_color(self):
        return self.__color
    
    def set_color(self, color):
        self.__color = color

auto = Auto('Volkswagen', '2023', 'Rojo')
#Obtener color
color = auto.get_color()
print(color)
#Cambiar localidad
auto.set_color('Azul')

auto.mostrar_datos()


class Auto:
    def __init__(self, marca, modelo, color, ciudad):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.__ciudad = ciudad
    def mostrar_datos(self):
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')
        print(f'Color: {self.color}')
        print(f'Ciudad: {self.ciudad}')

auto = Auto('Volkswagen', '2023', 'Rojo', 'CDMX')
auto.mostrar_datos()
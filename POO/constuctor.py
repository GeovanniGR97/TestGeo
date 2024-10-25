class Auto:
    
    #Constructor inicia con __init__
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        
    def mostra_datos(self):
        print(f"Autos: {self.marca}, Modelos: {self.modelo}, Color: {self.color}")

r1 = Auto('Volkswagen', '2024', 'Rojo')
r1.mostra_datos()

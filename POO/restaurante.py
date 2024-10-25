class Restaurante:
    def registro_platillos(self, comida_mexicana, comida_china, tacos):
        self.comida_mexicana = comida_mexicana
        self.comida_china = comida_china
        self.tacos = tacos
        print("Venta registrada")

    def imprimir(self):
        print("----Primer pago----")
        print(self.comida_mexicana)
        print(self.comida_china)
        print(self.tacos)
        print("-----C I E R R E-----")

restaurante = Restaurante()
restaurante.registro_platillos('GR01-001', 'GR01-002', 'GR03-003')
restaurante.imprimir()
mensaje = f"Venta exitosa de: {restaurante.comida_mexicana}, {restaurante.comida_china}, {restaurante.tacos}"
print(mensaje)
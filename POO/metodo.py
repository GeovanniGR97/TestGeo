#Un metodo es una funcion que esta dentro de una clase
class Comprobante:
    def registrar_venta(self, id_venta):
        self.id_venta_comprobante = id_venta
        print("Venta registrada..")

    def imprimir(self):
        print("***Primer resultado***")
        print(self.id_venta_comprobante)
        print("----------------------")


comprobante = Comprobante()
comprobante.registrar_venta('GR01-001')
comprobante.imprimir()
mensaje = f"Venta exitosa: {comprobante.id_venta_comprobante}"
print(mensaje)

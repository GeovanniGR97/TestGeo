def funcioConcatenacion():
    x = "hi"
    print(f"Hi" , x)
funcioConcatenacion()

def funcionReturn():
    return "Hola"
mensaje = funcionReturn()
print(mensaje)
funcionReturn()

listaFrutas = [1,2,3]
for i in listaFrutas:
    print(i)

datoTabla = int(input("Ingresa la tabla que deseas visualizar :"))
for i in range(1,101):
    resultado = i * datoTabla
    print(f"{datoTabla} * {i} = {resultado}")
    
    
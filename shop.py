print ("Datos del libro: ")
nombre = input("Escribe el nombre del libro: ")
idLibro = int(input("Escribe el id del libro: "))
precio = float(input("Proporciona el precio del libro: "))
envioGratuito = bool(input("Indica si es envio gratuito (True/False): " ))
if envioGratuito == 'True':
    envioGratuito == True
elif envioGratuito == 'False':
    envioGratuito = 'False'         
else:
    envioGratuito = 'Valor incorrecto debe de escribir True/False'

print (f'''
    Nombre : {nombre}
    Id libro : {idLibro},
    Precio: {precio},
    Envio gratuito?: {envioGratuito}
''')

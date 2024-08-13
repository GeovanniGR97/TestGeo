valor = int(input("Escribe el siguiente valor: "))
valorMinimo = 0
valorMaximo = 10
dentroRango = (valor >= valorMinimo) and (valor <= valorMaximo)
if dentroRango:
    print(f'El valor {valor} esta dentro de rango')
else:
   print(f'El valor {valor} esta fuera de rango')


    
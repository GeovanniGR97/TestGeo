costo = int(input('Cuanto dinero tienes para comer este mes: '))
if 0 <= costo <= 500:
    if costo < 100:
        mensaje = 'no vas a comer'
    elif 100 < costo < 200:
        mensaje = 'medio vas a comer'
    elif 200 < costo < 300:
        mensaje = 'espero que comas'
    elif 300 < costo < 400:
        mensaje = 'mas o menos vas a comer'
    elif 400 < costo <= 500:
        mensaje = 'Ya superaste el costo'
    else:
        mensaje= 'El rango que tienes de dinero supera lo que tienes para comer'      
        
    print(f'Tienes para comer: {costo}, {mensaje}')

else:
        print('no alcansa para comer')
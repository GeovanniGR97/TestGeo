#Conjunto de instrucciones que realizan un proceso 
#Su principal ventaja es que nos ayudan a evitar codigo repetido


sueldo = int(input("Ingresa tu sueldo :"))
def sueldoMexiano(sueldo):
    if sueldo > 1700:
        print(f"Tu sueldo es: {sueldo} ganas mas del sueldo mínimo")
    elif sueldo == 1750:
        print(f"Tu sueldo es: {sueldo} ganas el sueldo mínimo")
    else:
        print(f"Tu sueldo es: {sueldo} no ganas el sueldo minimo")
sueldoMexiano(sueldo)




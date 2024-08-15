''' Los diccionarios son estructuras de datos los cuales podemos almacenar
distintos valores
Los datos se almacenan asociados a una clave unica.
[clavevalor]: valor asociado
elementos almacenados estan en desorden, el oorden es indiferente a la forma de almacenamiento '''

miDiccionario = {"SINALOA":"MAZATLAN","CDMX": "EDOMEX","OAXACA":"OAXACA"} 
print(miDiccionario["OAXACA"])

miDiccionario["Tijuana"] = "Tijuana"
print(miDiccionario)

miDiccionario["CDMX"] = "Chilangolandia"
print(miDiccionario)

#Diccionario dentro de otro diccionario 
dataPersons = {"Apellido": "Rodriguez", "Anios":{1997,1998,1999,2000}}
print(dataPersons)
print(dataPersons["Anios"])
print(dataPersons.get('Apellido', "Jose"))
#En dado caso de no que la clave:valor no este mal escrito el valor asocidado se mostrara
print(dataPersons.get('Apellidos', "Jose"))
#Llaves principales de nuestra funcio
print(dataPersons.keys())
#Valores
valores = list(dataPersons.values())
print(valores)

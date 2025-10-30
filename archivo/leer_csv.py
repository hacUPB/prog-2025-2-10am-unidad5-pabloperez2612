import csv

with open("C:\\Users\\B09S202est\\Desktop\\archivo\\variable.csv", 'r') as csvfile:   #usamos el manejador de contexto
    lector = csv.reader(csvfile, delimiter=";")
    print(lector)
    encabezado = next(lector)
    presion=[]
    print(encabezado[0]) #se utiliza el método reader
    for fila in lector:    
        dato = float(fila[0])      #con el for se itera sobre el objeto para leer
        presion.append(dato)

print(presion)
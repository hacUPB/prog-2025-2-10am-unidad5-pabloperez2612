import csv

with open("C:\\Users\\B09S202est\\Desktop\\archivo\\variable.csv", 'r') as csvfile:   #usamos el manejador de contexto
    lector = csv.reader(csvfile, delimiter=";")
    print(lector)
    encabezado = next(lector)
    presion=[]
    print(encabezado[3]) #se utiliza el método reader
    for fila in lector:    
        fila[3] = fila[3].replace(",",".")
        dato = float(fila[3])      #con el for se itera sobre el objeto para leer
        presion.append(dato)

print(presion)
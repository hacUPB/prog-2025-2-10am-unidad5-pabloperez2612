import csv
lista = [1,2,3,4,5,6,7,8,9,10]
lista_2 = [2,4,6,8,10,12,14,16]
with open('salida.csv', 'w', newline='') as csvfile:
    escritor = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    escritor.writerow(['Nombre', 'Edad', 'Ciudad'])  # Escribe la fila de encabezados
    escritor.writerow(['John', 25, 'Nueva York'])
    escritor.writerow(['Jane', 30, 'Los Ángeles'])
    escritor.writerow(lista)
    escritor.writerow(lista_2)
lista = ["en las noches frias","no dice na","hablame 2","sexo quiero yo","soldado y profeta"]

ubicacion = "C:\\Users\\B09S202est\\Desktop\\archivo"
modo = "x"

nombre_archivo = "canciones.txt"
fp = open(ubicacion + "\\" + nombre_archivo, modo, encoding="utf-8")
for cancion in lista :
    fp.write(cancion+"\n")

fp.close()
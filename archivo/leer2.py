# abrir el archivo y definir el modo
archivo = open ("./archivo/ejercisio_1.txt", "r")
archivo.readline()
archivo.readline()
archivo.readline(11)
datos = archivo.readline()
archivo.close()
print(datos) 
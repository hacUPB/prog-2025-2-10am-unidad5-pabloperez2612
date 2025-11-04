# abrir el archivo y definir el modo
archivo = open ("./archivo/texto.txt", "r")
datos = archivo.readlines()
print(datos)
archivo.close()
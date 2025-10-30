ubicacion = "C:\\Users\\B09S202est\\Desktop\\archivo"

nombre_archivo = "frutas2.txt"
modo = "a" 
fp = open(ubicacion+"\\"+nombre_archivo, modo, encoding="utf-8")

frase = input("por favor ingrese una frase:")
edad = int(input("escribe la edad"))
estatura = float(input("ingrese su estatura"))
fp.write(frase)
fp.write(frase + "\n")
### el str sirve  para que el write lo reconozca
fp.write("\n")
fp.write(str(edad))
fp.write("\n")
fp.write(str(estatura))

fp.close()
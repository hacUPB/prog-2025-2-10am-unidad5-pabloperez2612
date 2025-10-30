import os
import csv
import matplotlib.pyplot as plt

#txt
def submenu_txt():
    archivo_txt = "maradona.txt"

    if not os.path.exists(archivo_txt):
        print(f" Error: No se encontró el archivo '{archivo_txt}'.")
        return

    with open(archivo_txt, 'r', encoding='utf-8') as fp:
        contenido = fp.read()

    print(f" Archivo '{archivo_txt}' cargado exitosamente.")
    while True:
        print("\n--- SUBMENÚ .TXT ---")
        print("1. Contar palabras y caracteres")
        print("2. Reemplazar una palabra")
        print("3. Histograma de vocales")
        print("4. Volver al menú principal")
        opcion_txt = input("Seleccione una opción: ")

        match opcion_txt:
            case '1':
                contar_palabras_caracteres(contenido)
            case '2':
                reemplazar_palabra(archivo_txt)
                with open(archivo_txt, 'r', encoding='utf-8') as fp:
                    contenido = fp.read()
            case '3':
                histograma_vocales(contenido)
            case '4':
                break
            case _:
                print("Opción no válida.")


def contar_palabras_caracteres(texto):
    palabras = texto.split()
    num_palabras = len(palabras)
    num_caracteres = len(texto)
    print(f"Número de palabras: {num_palabras}")
    print(f"Número de caracteres (incluyendo espacios): {num_caracteres}")


def reemplazar_palabra(filename):
    palabra_buscar = input("Palabra a buscar: ")
    palabra_reemplazar = input("Reemplazar por: ")

    with open(filename, 'r', encoding='utf-8') as fp:
        contenido = fp.read()

    nuevo_contenido = contenido.replace(palabra_buscar, palabra_reemplazar)

    with open(filename, 'w', encoding='utf-8') as fp:
        fp.write(nuevo_contenido)

    print(f" Se reemplazó '{palabra_buscar}' por '{palabra_reemplazar}' exitosamente.")


def histograma_vocales(texto):
    vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for char in texto.lower():
        if char in vocales:
            vocales[char] += 1

    print(f"Conteo de vocales: {vocales}")

    plt.figure(figsize=(8, 5))
    bars = plt.bar(vocales.keys(), vocales.values(), color='skyblue', edgecolor='black')
    plt.title('Histograma de Ocurrencia de Vocales')
    plt.xlabel('Vocal')
    plt.ylabel('Frecuencia')

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.2, int(yval),
                 ha='center', va='bottom')

    plt.show()

#csv
def submenu_csv():
    archivo_csv = "datos.csv"

    if not os.path.exists(archivo_csv):
        print(f" Error: No se encontró el archivo '{archivo_csv}'.")
        return

    print(f" Archivo '{archivo_csv}' cargado exitosamente.")

    while True:
        print("\n--- SUBMENÚ .CSV ---")
        print("1. Mostrar las filas del archivo")
        print("2. Graficar niveles del ICA")
        print("3. Volver al menú principal")
        opcion_csv = input("Seleccione una opción: ")

        match opcion_csv:
            case '1':
                mostrar_filas_csv(archivo_csv)
            case '2':
                graficar_ica(archivo_csv)
            case '3':
                break
            case _:
                print("Opción no válida. Intente nuevamente.")


def mostrar_filas_csv(filename):
    """Muestra las primeras filas del archivo CSV"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            print("\n--- CONTENIDO DEL ARCHIVO ---")
            for i, row in enumerate(reader):
                print(row)
                if i >= 14:
                    break
    except Exception as e:
        print(f" Error al leer el CSV: {e}")


def graficar_ica(filename):
    """Lee el CSV y grafica el nivel de calidad del aire (ICA)"""
    try:
        ica = []
        categorias = []

        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # saltar encabezado
            for row in reader:
                try:
                    valor = float(row[0])
                    ica.append(valor)
                    categorias.append(row[1])
                except ValueError:
                    continue

        if not ica:
            print(" No hay datos numéricos válidos en el archivo.")
            return

        # Asignar color según el valor de ICA
        colores = []
        for val in ica:
            if val <= 50:
                colores.append("green")
            elif val <= 100:
                colores.append("yellow")
            elif val <= 150:
                colores.append("orange")
            elif val <= 200:
                colores.append("red")
            elif val <= 300:
                colores.append("purple")
            else:
                colores.append("maroon")

        plt.figure(figsize=(10, 6))
        plt.bar(categorias, ica, color=colores, edgecolor='black')
        plt.title("Índice de Calidad del Aire (ICA)")
        plt.xlabel("Categoría de Calidad del Aire")
        plt.ylabel("Valor ICA")
        plt.xticks(rotation=20)
        plt.grid(True, axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f" Error al graficar: {e}")
# menu principal


def mostrar_menu_general():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Archivo de texto (.txt)")
    print("2. Archivo CSV (.csv)")
    print("3. Salir")
    return input("Seleccione una opción: ")


def main():
    while True:
        opcion = mostrar_menu_general()
        match opcion:
            case '1':
                submenu_txt()
            case '2':
                submenu_csv()
            case '3':
                print("👋 Saliendo del programa...")
                break
            case _:
                print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
import csv
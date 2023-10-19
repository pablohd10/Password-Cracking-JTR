import random

# Función para generar números aleatorios
def generar_numeros():
    return ''.join(str(random.randint(1, 4)) for _ in range(random.randint(1, 4)))

# Nombre del archivo de entrada y salida
archivo_entrada = "palabras1.txt"
archivo_salida = "palabras2.txt"

# Leer el archivo de entrada
with open(archivo_entrada, "r") as entrada:
    lineas = entrada.readlines()

# Generar los nuevos strings con números aleatorios
nuevas_lineas = [linea.strip() + generar_numeros() for linea in lineas]

# Escribir los resultados en el archivo de salida
with open(archivo_salida, "w") as salida:
    for linea in nuevas_lineas:
        salida.write(linea + "\n")

print(f"Proceso completado. Se han generado {len(nuevas_lineas)} líneas en {archivo_salida}.")

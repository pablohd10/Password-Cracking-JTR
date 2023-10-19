import random

# Lista de símbolos personalizada (sin letras ni números)
simbolos = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

# Nombre del archivo de entrada y salida
archivo_entrada = "palabras3.txt"
archivo_salida = "palabras4.txt"

# Leer el archivo de entrada
with open(archivo_entrada, "r") as entrada:
    lineas = entrada.readlines()

# Función para agregar un símbolo aleatorio al final de cada línea
def agregar_simbolo(cadena):
    simbolo = random.choice(simbolos)  # Elegir un símbolo de la lista
    return cadena.strip() + simbolo

# Agregar un símbolo al final de cada línea
nuevas_lineas = [agregar_simbolo(linea) for linea in lineas]

# Escribir los resultados en el archivo de salida
with open(archivo_salida, "w") as salida:
    for linea in nuevas_lineas:
        salida.write(linea + "\n")

print(f"Proceso completado. Se han generado {len(nuevas_lineas)} líneas en {archivo_salida}.")

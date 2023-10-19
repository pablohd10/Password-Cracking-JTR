import random

# Función para convertir en mayúscula una letra aleatoria
def convertir_letra_en_mayuscula(cadena):
    letras = [c for c in cadena if c.isalpha()]
    if letras:
        letra_aleatoria = random.choice(letras)
        cadena = cadena.replace(letra_aleatoria, letra_aleatoria.upper(), 1)
    return cadena

# Nombre del archivo de entrada y salida
archivo_entrada = "palabras2.txt"
archivo_salida = "palabras3.txt"

# Leer el archivo de entrada
with open(archivo_entrada, "r") as entrada:
    lineas = entrada.readlines()

# Asegurarse de que al menos una letra sea mayúscula en cada línea
nuevas_lineas = [convertir_letra_en_mayuscula(linea.strip()) for linea in lineas]

# Escribir los resultados en el archivo de salida
with open(archivo_salida, "w") as salida:
    for linea in nuevas_lineas:
        salida.write(linea + "\n")

print(f"Proceso completado. Se han generado {len(nuevas_lineas)} líneas en {archivo_salida}.")

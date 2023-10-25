import re
import os
import statistics

# Definir una función para convertir el formato de tiempo en segundos
def tiempo_a_segundos(tiempo):
    partes = tiempo.split(':')
    dias, horas, minutos, segundos = map(int, partes)
    return horas * 3600 + minutos * 60 + segundos

# Expandir el carácter tilde a la ruta completa del directorio de inicio
ruta_archivo_log = os.path.expanduser("~/.john/john.log")

# Leer el archivo de registro y buscar líneas que contienen "+ Cracked"
with open(ruta_archivo_log, "r") as archivo_log:
    lineas = archivo_log.readlines()

# Inicializar una lista para almacenar los tiempos en segundos
tiempos_en_segundos = []

# Buscar las líneas que contienen "+ Cracked" y extraer los tiempos
for linea in lineas:
    if "+ Cracked" in linea:
        tiempo_match = re.search(r"(\d+:\d+:\d+:\d+)", linea)
        if tiempo_match:
            tiempo = tiempo_match.group(1)
            tiempos_en_segundos.append(tiempo_a_segundos(tiempo))

# Calcular la media de los tiempos en segundos
if tiempos_en_segundos:
    media = sum(tiempos_en_segundos) / len(tiempos_en_segundos)
    print(f"Media de los tiempos en segundos: {media:.2f}")
    mediana = statistics.median(tiempos_en_segundos)
    print(f"Mediana de los tiempos en segundos: {mediana:.2f}")
else:
    print("No se encontraron tiempos para calcular la media.")

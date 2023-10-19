import random
import string

def generar_numeros():
    longitud = 7
    numeros = string.ascii_lowercase 
    return ''.join(random.choice(numeros) for _ in range(longitud))

# Generar la lista de strings
lista_de_numeros = [generar_numeros() + "\n" for _ in range(100)]

# Unir la lista en una sola cadena
resultado = ''.join(lista_de_numeros)

# Guardar el resultado en un archivo .txt
nombre_archivo = "min5.txt"
with open(nombre_archivo, "w") as archivo:
    archivo.write(resultado)

print(f"Se ha guardado el resultado en {nombre_archivo}")
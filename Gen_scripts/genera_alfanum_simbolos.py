import random
import string

def generar_cadena():
    longitud = 7
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longitud))

# Generar la lista de strings
lista_de_strings = [generar_cadena() + "\n" for _ in range(100)]

# Unir la lista en una sola cadena
resultado = ''.join(lista_de_strings)

# Guardar el resultado en un archivo .txt
nombre_archivo = "alfanum_simb5.txt"
with open(nombre_archivo, "w") as archivo:
    archivo.write(resultado)

print(f"Se ha guardado el resultado en {nombre_archivo}")
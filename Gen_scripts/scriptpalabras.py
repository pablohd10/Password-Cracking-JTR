import nltk
import random

# Descarga los datos necesarios para generar palabras reales
nltk.download("words")

from nltk.corpus import words

# Obtiene una lista de palabras reales disponibles en el diccionario de palabras de nltk
word_list = words.words()

# Genera 100 palabras aleatorias
random_words = random.sample(word_list, 100)

# Abre el archivo "palabras1.txt" en modo escritura y guarda las palabras
with open("palabras1.txt", "w") as file:
    for word in random_words:
        file.write(word.lower() + "\n")

print("Se han generado y guardado 100 palabras en el archivo 'palabras1.txt'.")

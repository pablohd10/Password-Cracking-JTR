# Leer el archivo de entrada y generar el archivo de salida
with open("palabras1.txt", "r") as input_file, open("palabras5.txt", "w") as output_file:
    for line in input_file:
        word = line.strip()  # Leer cada línea del archivo de entrada
        transformed_word = word.upper() + word.upper()  # Concatenar la palabra con su versión en mayúsculas
        output_file.write(transformed_word + "\n")  # Escribir la palabra transformada en el archivo de salida

print("Transformación completada. Las palabras transformadas se han guardado en 'output.txt'.")

import hashlib

# Función para hashear una contraseña con SHA-256
def hashear_contrasena(contrasena):
    # Crear un objeto hash SHA-256
    sha256 = hashlib.sha256()
    # Actualizar el objeto hash con la contraseña
    sha256.update(contrasena.encode('utf-8'))
    # Obtener el hash en formato hexadecimal
    hashed_password = sha256.hexdigest()
    return hashed_password

# Archivo de entrada y salida
archivo_entrada = "palabras5.txt"
archivo_salida = "palabras_hashed_5.txt"

# Procesar el archivo de entrada y generar el archivo de salida con las contraseñas hasheadas
try:
    with open(archivo_entrada, "r") as entrada, open(archivo_salida, "w") as salida:
        for linea in entrada:
            # Limpia la línea de cualquier carácter no deseado (por ejemplo, saltos de línea)
            linea = linea.strip()
            # Hashea la contraseña con SHA-256
            hashed_password = hashear_contrasena(linea)
            # Escribe la contraseña hasheada en el archivo de salida
            salida.write(hashed_password + '\n')
    print(f"Las contraseñas se han hasheado correctamente con SHA-256 y se han guardado en '{archivo_salida}'.")
except FileNotFoundError:
    print(f"El archivo '{archivo_entrada}' no fue encontrado.")
except Exception as e:
    print(f"Ocurrió un error: {str(e)}")
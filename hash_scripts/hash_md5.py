import hashlib

# Función para hashear una contraseña con MD5
def hashear_contrasena(contrasena):
    # Crear un objeto hash MD5
    md5 = hashlib.md5()
    # Actualizar el objeto hash con la contraseña
    md5.update(contrasena.encode('utf-8'))
    # Obtener el hash en formato hexadecimal
    hashed_password = md5.hexdigest()
    return hashed_password

# Archivo de entrada y salida
archivo_entrada = "minus_7.txt"
archivo_salida = "minus_md5_7.txt"

# Procesar el archivo de entrada y generar el archivo de salida con las contraseñas hasheadas
try:
    with open(archivo_entrada, "r") as entrada, open(archivo_salida, "w") as salida:
        for linea in entrada:
            # Limpia la línea de cualquier carácter no deseado (por ejemplo, saltos de línea)
            linea = linea.strip()
            # Hashea la contraseña con MD5
            hashed_password = hashear_contrasena(linea)
            # Escribe la contraseña hasheada en el archivo de salida
            salida.write(hashed_password + '\n')
    print(f"Las contraseñas se han hasheado correctamente con MD5 y se han guardado en '{archivo_salida}'.")
except FileNotFoundError:
    print(f"El archivo '{archivo_entrada}' no fue encontrado.")
except Exception as e:
    print(f"Ocurrió un error: {str(e)}")

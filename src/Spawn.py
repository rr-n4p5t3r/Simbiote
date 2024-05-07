# Spawn.py
# Hace lo contrario a HellSpawn, descifra el contenido cifrado con la llave generada previamente.

import os
from cryptography.fernet import Fernet

def decrypt_file(encrypted_file_path, key):
    """Descifra un archivo cifrado.

    Lee el contenido de un archivo cifrado, lo descifra utilizando una clave proporcionada
    y guarda el contenido descifrado en un nuevo archivo con la extensión '.encrypted'
    eliminada.

    Args:
        encrypted_file_path (str): Ruta del archivo cifrado a descifrar.
        key (bytes): Clave de cifrado utilizada para descifrar el archivo.
    """
    with open(encrypted_file_path, 'rb') as f:
        encrypted_data = f.read()
    
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)
    
    original_file_path = encrypted_file_path.replace('.encrypted', '')
    with open(original_file_path, 'wb') as f:
        f.write(decrypted_data)

if __name__ == "__main__":
    # Especifica el directorio que quieres descifrar
    directorio_a_descifrar = r"D:\dev\proyectos\ciberseguridad\Simbiote\src"
    
    # Clave de cifrado
    key = input("Ingrese la clave de cifrado: ")
    
    # Descifrar los archivos en el directorio especificado
    for root, dirs, files in os.walk(directorio_a_descifrar):
        for file in files:
            if file.endswith('.encrypted'):
                file_path = os.path.join(root, file)
                decrypt_file(file_path, key)
    
    print(f"Simbiote ha descifrado los archivos en {directorio_a_descifrar} con éxito.")

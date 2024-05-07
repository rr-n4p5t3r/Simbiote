# Venom.py
# Simbiote que replica N elevado a la N, todos los archivos de un directorio especifico de un disco duro

import os
import shutil

def replicate(directory):
    """Replica todos los archivos de un directorio.

    Esta función recibe como entrada un directorio y replica cada archivo dentro
    del mismo directorio una cantidad de veces igual al número total de archivos
    presentes en el directorio.

    Args:
        directory (str): Ruta del directorio que se replicará.
    """
    # Obtener la lista de archivos en el directorio especificado
    files = os.listdir(directory)
    total_files = len(files)
    
    # Obtener la ubicación actual del script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Crear replicas de los archivos en el mismo directorio
    for file in files:
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):  # Solo copiar archivos, no directorios
            # Calcular el número de réplicas para este archivo
            replicas = total_files ** total_files
            for i in range(replicas):
                new_file_name = f"{os.path.splitext(file)[0]}_{i}{os.path.splitext(file)[1]}"
                new_file_path = os.path.join(current_dir, new_file_name)
                shutil.copy(file_path, new_file_path)
    
    print(f"Simbiote ha replicado los archivos con éxito. Se han creado un total de {total_files ** total_files} réplicas por cada archivo.")

if __name__ == "__main__":
    # Especifica el directorio que quieres replicar
    directorio_a_replicar = r"D:\dev\proyectos\ciberseguridad\Simbiote\src"
    replicate(directorio_a_replicar)

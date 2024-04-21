# Simbiote

Simbiote es una suite de herramientas de ciberseguridad diseñada para la replicación y el cifrado de archivos en sistemas de almacenamiento de datos. Este proyecto ofrece una serie de herramientas que permiten replicar archivos en discos duros y directorios específicos, así como cifrar y descifrar archivos utilizando técnicas de cifrado seguro.

## Funcionalidades

### Carnage.py

**Carnage.py** es una implementación de Simbiote que permite la replicación de archivos en un disco duro. Utiliza un algoritmo que replica cada archivo presente en el disco duro elevado a la potencia de la cantidad total de archivos en el disco. Esto resulta en una replicación masiva de archivos que puede ayudar en la preservación y protección de datos en sistemas de almacenamiento local.

### HellSpawn.py

**HellSpawn.py** es una herramienta de Simbiote diseñada para cifrar el contenido de un directorio utilizando una clave de cifrado generada previamente. Utiliza la biblioteca de criptografía Fernet para cifrar los archivos presentes en el directorio, garantizando así la confidencialidad de los datos almacenados. Esta herramienta proporciona una capa adicional de seguridad para proteger la información sensible.

### Spawn.py

**Spawn.py** es la contraparte de HellSpawn.py. Esta herramienta se encarga de descifrar el contenido cifrado previamente utilizando la clave de cifrado generada por HellSpawn.py. Al descifrar los archivos, permite restaurar el contenido original del directorio, lo que facilita el acceso a los datos para los usuarios autorizados.

### Venom.py

**Venom.py** es otra implementación de Simbiote que replica archivos, pero esta vez en un directorio específico de un disco duro. Similar a Carnage.py, replica cada archivo presente en el directorio especificado elevado a la potencia de la cantidad total de archivos en el directorio. Esta herramienta proporciona una forma eficiente de replicar archivos en directorios específicos para mantener la integridad y disponibilidad de los datos.

## Contribución

Las contribuciones son bienvenidas. Si deseas contribuir al proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Clona tu fork en tu máquina local.
3. Crea una nueva rama para tu contribución (`git checkout -b feature/nueva-funcionalidad`).
4. Realiza tus cambios y haz commits (`git commit -am 'Agrega nueva funcionalidad'`).
5. Haz push a tu rama (`git push origin feature/nueva-funcionalidad`).
6. Abre un pull request en GitHub.

## Licencia

Este proyecto está licenciado bajo la [Licencia Pública General de GNU, versión 3 (GNU GPLv3)](LICENSE).

## Autor

**Ricardo Rosero**  
Email: rrosero2000@gmail.com  
GitHub: [rr-n4p5t3r](https://github.com/rr-n4p5t3r)

### Invítame un café: ###

<div id="badges">
  <a href="https://www.buymeacoffee.com/elblogden4p5t3r" target="_blank">
    <img src="https://img.shields.io/badge/buymeacoffee-yellow?style=for-the-badge&logo=buymeacoffee&logoColor=white" alt="LinkedIn Badge"/>
  </a>
</div>

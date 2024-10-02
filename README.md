# Superando el reto del billón de filas con Python

## Preparación imprescindible antes del taller

**NO VAMOS A DEDICAR TIEMPO A LA INSTALACIÓN DURANTE EL TALLER ASÍ QUE, POR FAVOR, VEN CON TODO INSTALADO PREVIAMENTE.**

1. Descargar el repositorio en local.
1. Descargar Miniforge: https://conda-forge.org/miniforge/.
1. Ejecutar el instalador de Miniforge adecuado según tu sistema operativo.
1. Crear del entorno virtual: ``conda env create -f environment.yml``.
1. Descargar el siguiente fichero comprimido con todos los archivos necesarios: https://drive.google.com/file/d/1mVzfZ3ysi2dABFjYLi041Rs-SqqA_DNh/view?usp=share_link (524 MB).
2. Descomprimir el contenido del fichero anterior en la carpeta ``data``.

## Abstract 

En el mundo del análisis de datos nos encontramos a menudo con la necesidad de analizar una cantidad masiva de datos con unos recursos muy limitados y en estos casos es importante tener claro qué estrategias y librerías se adaptan mejor a nuestras necesidades.

En este tutorial práctico vamos a cargar un fichero con mil millones de filas, inspirándonos en el reto de procesar un billón (en inglés) de filas: https://github.com/gunnarmorling/1brc, y veremos cómo podemos procesarlo y trabajar con él mediante Python.

En concreto, para superar este reto trabajaremos con librerías como numpy, pandas, Polars, PyArrow, DuckDB, Dask o Modin y utilizaremos formatos de ficheros tales como CSV, Apache Parquet o Feather y veremos las ventajas y desventajas de cada opción.

Para poder aprender y disfrutar de este tutorial recomendamos tener al menos 1 año de experiencia en Python, pero no es necesario tener experiencia en procesamiento de grandes cantidades de datos. Y no te preocupes si tienes un portátil con pocos recursos porque podrás adaptar fácilmente el tutorial a tu configuración y completar todos los ejercicios que te planteamos sin problema.
    
## Distribución del tiempo

- **Presentaciones y bienvenida (2 min)**  
- **Introducción al tutorial y objetivos (2 min)**
- **Almacenamiento en memorias secundarias (10 min)**  
- **Carga de datos desde memorias secundarias a principales (20 min)**  
- **Ejercicios sobre carga de datos (10 min)**  
- **Ejecución de operaciones sobre datos en memoria principal (20 min).**
- **Ejercicios sobre ejecución de operaciones (10 min)**  

## Tutorial

Los pasos que vamos a seguir en el tutorial son los siguientes:

1. Abrir una terminal y situarse dentro de la carpeta de tutorial: ``cd PyConES2024_Superando_el_1brc_con_Python``
1. Activación del entorno virtual: ``conda activate 1brc``.
1. Ejecución de JupyterLab: ``jupyter lab``.
1. Tipos de datos: fichero ``1_tipos_de_datos.ipynb``.
1. Lectura de ficheros en la memoria principal: fichero ``2_leyendo_datos.ipynb``.
1. Ejecución de operaciones sobre los ficheros cargados: fichero ``3_consultando_datos.ipynb``.

NOTA: en caso de tener problemas con la terminal del sistema os recomnedamos usar la terminal de Miniforge (Miniforge Prompt).

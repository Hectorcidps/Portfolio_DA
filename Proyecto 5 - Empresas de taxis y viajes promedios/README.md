# Proyecto 5 - Empresas de taxis y viajes promedio realizados 🚕🚕

## Descripción:
1. Primer parte del proyecto, desarrollado con SQL:
Una empresa de viajes compartidos en Chicago, necesita que se encuentren los patrones de información disponible para comprender las preferencias de los pasajeros y el impacto de los factores externos en los viajes.
2. Segunda parte del proyecto desarrollado con Python:
A partir de 3 tablas obtenidas con SQL realizar un análisis enfocados en identificar tendencias clave, como los barrios y las empresas con mayor número de viajes concluidos. Verificación y eliminación de outliers para asegurar resultados precisos en la comprobación de la hipótesis, la cual consiste en saber si existe una relación entre la duración de los viajes con el clima de la ciudad.

## 🛠️ Tecnologías implementadas
* Lenguajes de Programación: Python y SQL
* Librería de extracción de datos: BeautifulSoup 
* Librerías de limpieza y manipulación de datos: Pandas, NumPy
* Librerias de pruebas estadísticas: SciPy, Stats
* Librerías de visualización de datos: Matplotlib, Seaborn 
* DBMS: PostgreSQL

## 📈 Competencias
* Limpieza y Preparación de Datos
* Visualización y Reporte de Datos
* Comprobación de hipótesis mediante pruebas estadísticas 
* Conexión a una base de datos en PostgreSQL 
* Extacción de datos
* Consultas y Subqueries SQL

## Características Principales:
1. Extracción de datos: implementando el método GET en Python y la librería BeautifulSoup para navegar en el HTML y extraer datos relevantes.

2. SQL: Limpiar los datos utilizando SQL, usando comandos básicos como SELECT, FROM, WHERE, así como funciones más avanzadas como HAVING, OVER, subconsultas (subqueries), y JOINS. También eliminar valores duplicados y ausentes para mantener la integridad del análisis.

3. Análisis en Python: Con las tres tablas realizar un análisis en Python, centrado en:

* Identificar los 10 barrios con mayor número de viajes concluidos.
* Determinar las 10 empresas con mayor número de viajes.
* Detectar y eliminar outliers para evitar sesgos en los resultados.
* Comprobar una hipótesis sobre el impacto del clima en la duración de los viajes.

### Hipótesis:
* Hipótesis: La duración promedio de los viajes desde el Loop hasta el Aeropuerto Internacional O'Hare cambia los sábados lluviosos
H0: La duración promedio de los viajes desde el Loop hasta el Aeropuerto Internacional O'Hare NO cambia en los sábados lluviosos
H1: La duración promedio de los viajes desde el Loop hasta el Aeropuerto Internacional O'Hare cambia en los sábados lluviosos

## Resultados:
Con este análisis se lograron identificar que los barrios Loop, River North, Streeterville y West Loop, son los que cuentan con mejores promedios en su finalización de viajes, aunque se encontraron otros 6 barrios más, estos tienen un promedio muy bajo comparado con los antes mencionados. Por la parte de las empresas con mayores números de viajes realizados, se encontró que Flash Cab es el que tiene un domino en la zona donde se realizó el análisis, sin embargo, existen otras empresas ubicadas en el top 10 pero estas cuentan con un promedio similar tal es el caso de Yellow Cab y Sun Taxi las cuales tienen un promedio de 10,000 viajes concluidos.

En cuanto a la hipótesis se puede mencionar, que para comprobarla se realizó una prueba T de Student para muestras independientes y además se realizó una prueba de Levene para comprobar que las varianzas de los datos fuera igual, así pues de acuerdo a los datos, se concluyo que existen diferencias significativas en el promedio de tiempo de los viajes los días sábados lluviosos, es decir, que en presencia de lluvia el tiempo de duración tiende a cambiar en comparación a los dias que no hay presencia de lluvia. 

### Enlace al proyecto(Python): [Haz click aquí](https://github.com/Hectorcidps/Portfolio_DA/blob/master/Proyecto%205%20-%20Empresas%20de%20taxis%20y%20viajes%20promedios/Empresas%20de%20taxis.ipynb) 

### Enlace al proyecto(SQL): [Haz click aquí](https://github.com/Hectorcidps/Portfolio_DA/blob/master/Proyecto%205%20-%20Empresas%20de%20taxis%20y%20viajes%20promedios/codigo_sql.sql)

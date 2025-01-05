# Proyecto Final - Consultas SQl con conexión a BD PostgreSQL

##  Descripción: 
El coronavirus tomó al mundo entero por sorpresa, cambiando la rutina diaria de todos y todas. Los habitantes de las ciudades ya no pasaban su tiempo libre fuera, yendo a cafés y centros comerciales; sino que más gente se quedaba en casa, leyendo libros. Eso atrajo la atención de las startups (empresas emergentes) que se apresuraron a desarrollar nuevas aplicaciones para los amantes de los libros.

Te han dado una base de datos de uno de los servicios que compiten en este mercado. Contiene datos sobre libros, editoriales, autores y calificaciones de clientes y reseñas de libros. Esta información se utilizará para generar consultas sobre los libros más populares, las editoriales y autores más relevantes. 

## Características Principales: 

* Conexión a una base de datos en PostgreSQL 
* Creación de una función para explorar tablas 
* Creación de una función para mostrar resultados con Pandas
* Exploración de tablas 
* Consulta sobre los libros publicados después del 1 de enero de 2000
* Consulta para identificar el número de reseñas de usuarios y la calificación promedio de cada libro 
* Consulta para identificar la editorial con mayor número de libros y con más de 50 páginas.
* Consulta para identificar al autor con la calificación promedio más alta en sus libros. 
* Consulta para conocer el número promedio de reseñas de texto entre los usuarios que calificacon más de 50 libros. 

## Resultados:
Consulta 1: Se encontraron un total de 819 libros publicados después del 1 de enero de 2000.

Consulta 2: En esta consulta se aprecia que el promedio mas alto de calificacion es de 5 para diferentes libros, mientras que el numero de reseñas varia, además se observa que algunos titulos cuentan con un mayor numero de reseñas y esto se ve reflejado en la calificacion promedio del libro, siendo mas bajo que aquellos que presentan menos reseñas de usuarios

Consulta 3: La editorial con mayor número de libros publicados con mas de 50 páginas es Penguin Books con un total de 42 libros publicados, seguido de Vintage con 31 libros y Grand Central Publishing con 25 libros.

Consulta 4: La autora con la mas alta calificación promedio por libro es Diana Gabaldon con un promedio de 4.3 y un total de 50 calificaciones recibidas, sin embargo, J.K. Rowling y Mary GrandPré cuentan con un mayor numero de calificaciones recibidas y estan muy cerca en cuanto a promedio de la autora Diana.

Consulta 5: Por último se cálculo el promedio de reseñas de texto entre los usuarios que han calificado mas de 50 libros y esto dio como resultado 24.33 reseñas de texto por usuario.

## 🛠️ Tecnologías implementadas
* Lenguajes de Programación: SQL
* Preparación de los datos: SQL 
* DBMS: PostgreSQL
* Librería de manipulación de datos: Pandas

## 📈 Competencias
* Conexión a una base de datos en PostgreSQL 
* Extacción de datos
* Consultas SQL
* Consultas implementando subqueries


### Enlace al proyecto: [Haz click aquí](https://github.com/Hectorcidps/Portfolio_DA/blob/master/Proyecto%20final/Proyecto%20SQL/SQL.ipynb)
# Proyecto Final - Test A/B: Tienda online de sandias

##  Descripción: 
Has recibido una tarea analítica de una tienda en línea internacional. Tus predecesores no consiguieron completarla: lanzaron una prueba A/B y luego abandonaron (para iniciar una granja de sandías en Brasil). Solo dejaron las especificaciones técnicas y los resultados de las pruebas esperadas. 

### Descripción técnica
    * Nombre de la prueba: recommender_system_test
    * Grupos: А (control), B (nuevo embudo de pago)
    * Launch date: 2020-12-07
    * Fecha en la que dejaron de aceptar nuevos usuarios: 2020-12-21
    * Fecha de finalización: 2021-01-01
    * Audiencia: 15% de los nuevos usuarios de la región de la UE
    * Propósito de la prueba: probar cambios relacionados con la introducción de un sistema de recomendaciones mejorado
    * Resultado esperado: dentro de los 14 días posteriores a la inscripción, los usuarios mostrarán una mejor conversión en vistas de la página del producto (el evento product_page), instancias de agregar artículos al carrito de compras (product_card) y compras (purchase). En cada etapa del embudo product_page → product_card → purchase, habrá al menos un 10% de aumento.
   * Número previsto de participantes de la prueba: 6 000

## Características Principales: 

* Análisis exploratorio de los datos 
* Limpieza y manipulación de datos 
* Análisis de valores atípicos
* Estudio de la conversión de clientes en diferentes etapas dem embudo de eventos
* Análisis de distribución de muestras 
* Resultados de prueba A/B mediante pruebas estadísticas

## Resultados: 
Al realizar el EDA, se identificó que las muestras no estaban distribuidas equitativamente, ya que el grupo A contaba con un 56.6%, mientras que el grupo B representaba un 43.4%. Esto resultó en una diferencia del 13.2%, lo cual indica una mayor representación del grupo A, lo que podría influir en los resultados y dificultar una comparación directa.
Por otra parte, al analizar el embudo sin división de grupos, se encontró que solo una etapa (login) superaba el 10% de tasa de conversión; sin embargo, el resto de las etapas no alcanzaron este umbral. Al construir un embudo con las etapas esperadas, se obtuvo un resultado aún menos favorable: ninguna etapa logró superar el 10% de tasa de conversión. En concreto, se observó que solo el 56.82% de los usuarios realiza la acción de visitar la página del producto (product_page), apenas el 6.99% añade productos al carrito (product_cart), y solo el 0.03% de los usuarios iniciales completa una compra.

También se encontró que 441 usuarios estaban presentes en ambas muestras. Además, al analizar la distribución de los datos respecto al número de eventos por usuario, se identificaron numerosos valores atípicos. La media del total de eventos por usuario es de 7.2; al calcular los percentiles, se obtuvo que el 10% de los usuarios realiza 12 eventos, el 5% realiza 15 eventos y solo el 1% realiza 20 eventos. El número máximo de eventos registrados por usuario es 36.

Asimismo, se analizó la distribución de los datos respecto a las compras realizadas por usuario. En este caso, también se identificaron muchos valores atípicos. Algo notable es que un gran número de usuarios no realizó compras; durante el preprocesamiento, se encontró que había 363,447 usuarios en esta categoría, lo cual se refleja en la distribución. Sin embargo, entre los usuarios que realizaron compras, los valores son dispersos. La media del gasto por usuario es de 24.53 USD. En los percentiles, se encontró que el 10% de los usuarios gastó 39.93 USD, el 5% gastó 114.97 USD y solo el 1% gastó 514.97 USD. El gasto máximo registrado fue de 1,609.94 USD.

Al realizar la prueba A/B, se calculó la tasa de conversión para ambas muestras. Los resultados no fueron los esperados, ya que en las 4 etapas no se alcanzó la meta establecida (solo la etapa de product_cart se acerco obteniendo un 9.65%), que consistía en un aumento de al menos el 10% en cada etapa del embudo. Sin embargo, el número de usuarios participantes sí cumplió con los objetivos, ya que en ambos grupos hubo más de 6,000 participantes. Finalmente, al calcular la significancia estadística de la distribución de las muestras, con un nivel de significancia del 0.05, se obtuvo un valor p de 0.0006. Esto indica que se debe rechazar la hipótesis nula, lo que confirma que existe una diferencia significativa entre las muestras.

## 🛠️ Tecnologías implementadas
* Lenguajes de Programación: Python
* Librería de limpieza y manipulación de datos: Pandas
* Librerias de visualización: Matplotlib, Seaborn
* Librerias de pruebas estadísticas: SciPy, Stats

## 📈 Competencias
* Limpieza y Preparación de Datos
* Visualizacion de graficos
* Análisis de embudo de eventos
* Pruebas A/B
* Comprobación de hipótesis 

### Enlace al proyecto: [Haz click aquí](https://github.com/Hectorcidps/Portfolio_DA/blob/master/Proyecto%20final/Proyecto%20Test%20A%20B/Test%20A%20B.ipynb)
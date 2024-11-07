# Proyecto 7 - Experimento A/B 🧪🧪  

## Descripción: 
Una gran tienda online ha recopilado una lista de hipótesis que pueden ayudar a aumentar los ingresos. El objetivo es priorizar estas hipótesis, lanzar un test A/B y analizar los resultados. 

## Características Principales: 
La primera etapa de este proyecto consistió en priorizar nueve hipótesis sobre cómo aumentar los ingresos de una tienda en línea, aplicando los frameworks ICE y RICE. La segunda etapa comenzó tras identificar las hipótesis principales; en esta fase se realizó un análisis de prueba A/B, donde se calcularon métricas como el ingreso acumulado por grupo, el tamaño promedio de pedido por grupo, la tasa de conversión de cada grupo y la significancia estadística entre los grupos, utilizando tanto datos brutos como datos filtrados (eliminando valores atípicos que pudieran afectar el análisis). Finalmente, se tomó una decisión fundamentada en los datos obtenidos de la prueba.

## Resultados:
Durante este análisis, se encontró que las hipótesis con mayor puntaje en el framework ICE fueron: la hipótesis 9, que propone "Lanzar una promoción que ofrezca a los usuarios descuentos en sus cumpleaños"; la hipótesis 1, cuyo supuesto es "Añadir dos nuevos canales para atraer tráfico, lo cual traerá un 30% más de usuarios"; y la hipótesis 8, que sugiere "Añadir un formulario de suscripción a todas las páginas principales para crear una lista de correo". Al analizar estas hipótesis, se observa que son acciones comunes en muchas empresas, lo que las convierte en antecedentes sólidos para avanzar al test A/B.

En cuanto a las hipótesis con mayor puntaje en el framework RICE, coincidieron dos con las seleccionadas por ICE: la hipótesis 1 y la hipótesis 8, cuyos supuestos ya se conocen. A estas se suma la hipótesis 3, que plantea "Agregar bloques de recomendaciones de productos en el sitio de la tienda para aumentar la conversión y el tamaño promedio de compra".

Los resultados de cada framework muestran que RICE considera el alcance y, por lo tanto, puede dar prioridad a hipótesis con un mayor impacto potencial en el público. Sin embargo, las hipótesis con un gran impacto pero un alcance menor tienden a bajar en la clasificación cuando se utiliza RICE.

Al realizar el test A/B, y tras calcular el ingreso acumulado por grupo, el tamaño promedio de pedido y la tasa de conversión de cada grupo, se determinó que el experimento B es superior, ya que mostró un mayor ingreso, alcanzando hasta un 16% más en el tamaño promedio de pedido que el experimento A. En cuanto a la tasa de conversión, el grupo B alcanzó un máximo del 36% y se mantuvo por encima del 30% hasta el final del ciclo de vida.

Para evaluar la significancia estadística, se utilizó la prueba U de Mann-Whitney, obteniendo los siguientes resultados: en el análisis del test utilizando datos brutos, el experimento B presentó un 13.8% más de ganancia en la tasa de conversión en comparación con el grupo A. Además, el grupo B registró un 25.2% más en el tamaño promedio de pedidos, aunque el valor p fue de 0.692 frente a un nivel de significancia de 0.05, indicando que el resultado no es estadísticamente significativo. 
Con los datos filtrados (eliminando valores atípicos), el grupo B mostró una ganancia relativa del 17% en la tasa de conversión frente al grupo A, pero al analizar el tamaño promedio de pedidos, el grupo B obtuvo una diferencia relativa del 2.8% menor, lo que indica que esta variación no afecta significativamente el tamaño promedio de los dos grupos.

En conclusión, sería recomendable continuar con la prueba, ya que esto podría ayudar a identificar si el grupo B consolida su desempeño en ambas métricas (conversión y tamaño de pedido).

## 🛠️ Tecnologías implementadas
* Lenguajes de Programación: Python
* Análisis de Datos: pandas, numpy, scipy
* Comprobación de hipótesis: stats
* Visualización de Datos: matplotlib, seaborn

## 📈 Competencias
* Limpieza y Preparación de Datos
* Calculo de metricas relevantes
* Calculo de ICE y RICE 
* Visualización y Reporte de Datos
* Toma de decisiones basadas en datos
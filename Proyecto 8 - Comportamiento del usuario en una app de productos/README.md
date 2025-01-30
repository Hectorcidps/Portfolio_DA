# Proyecto 8 - Comportamiendo del usuario/usuaria en una app de productos 👩🧑🍎🛒

## Descripción: 
Este proyecto analizó más de 244,000 eventos para entender el flujo de interacción de los usuarios y evaluar un experimento A/A/B. Se construyó un embudo de conversión, identificando etapas clave de pérdida de usuarios y oportunidades de optimización. Además, se aplicaron pruebas estadísticas como el puntaje Z y la prueba U de Mann-Whitney, confirmando que los grupos analizados tenían distribuciones similares.

## 🛠️ Tecnologías implementadas
* Lenguajes de Programación: Python
* Librerías de limpieza y manipulación de datos: Pandas, NumPy
* Librerias de pruebas estadísticas: SciPy, Stats
* Librerías de visualización de datos: Matplotlib, Seaborn 

## 📈 Competencias
* Limpieza y Preparación de Datos
* Visualización y Reporte de Datos
* Funnel de eventos
* Pruebas A / B
* Comprobación de hipótesis con pruebas estadísticas
* Toma de decisiones basadas en datos

## Características Principales: 

Este proyecto consistió en el análisis de eventos generados por usuarios en una app, con el objetivo de identificar patrones de comportamiento, optimizar el flujo de interacción y evaluar la efectividad de un experimento A/B.

Durante el preprocesamiento de datos, se detectaron y analizaron valores duplicados, los cuales reflejaban interacciones de los usuarios en múltiples etapas del funnel. El dataset incluyó más de 244,000 eventos registrados entre julio y agosto de 2019, de los cuales el 98.84% correspondieron al período de agosto, que fue tomado como base para el análisis.

Además, se evaluó la pérdida de usuarios en cada fase del embudo, detectando que las mayores fugas ocurrían entre el carrito de compras y la finalización del pago. Este hallazgo brinda información clave para mejorar la experiencia del usuario y aumentar la conversión.

El análisis estadístico incluyó pruebas como el puntaje Z y la prueba U de Mann-Whitney para comparar las proporciones y distribuciones entre los grupos de control y experimental. 

Finalmente, se aplicó la corrección de Bonferroni para garantizar la validez de las conclusiones.

## Resultados:
En la etapa de preprocesamiento de los datos se halló que los tres grupos contaban con valores duplicados. Esto puede deberse a que los usuarios interactuaron con más de una etapa del funnel.
Durante el análisis de los eventos, se encontró un total de 244,126 eventos divididos en cinco tipos:

* Main Screen Appear - con un total de: 119,205
* Offers Screen Appear - con un total de: 46,825
* Cart Screen Appear - con un total de 42,731
* Payment Screen Successful - con un total de: 34,313
* Tutorial - con un total de: 1,052

En cuanto a los usuarios, se encontró un total de 7,551 usuarios únicos divididos por tipo de evento:

* Main Screen Appear: con un total de 7439
* Offers Screen Appear: con un total de 4613
* Cart Screen Appear: con un total de 3749
* Payment Screen Successful: con un total de 3547
* Tutorial: con un total de 847

Después, se identificó que el período total de los datos (del 25/07/2019 al 07/08/2019) muestra que julio no representa los datos de manera significativa, pues solo tiene el 1.16% del total, mientras que agosto cuenta con el 98.84%. Por lo tanto, el análisis se basa en el período con mayor cantidad de datos. En agosto se registraron 241,298 eventos y un total de 7,534 usuarios.

Para identificar la frecuencia de eventos fue necesario construir un embudo, en el cual se observa que las fases tienen un orden: comenzando por Main Screen, siguiendo con Offer Screen, Cart Screen y Payment Screen. Este patrón es común y se observa en muchos sitios web. Sin embargo, la parte final del embudo, es decir, el evento Tutorial, es el que tiene menor frecuencia. Esto podría indicar que muchos usuarios omiten esta fase o la desconocen.

El siguiente paso consistió en calcular las proporciones de los usuarios que realizaron al menos una acción, obteniendo los siguientes resultados:

* El 98.47% de los usuarios ingresaron a la página principal.
* El 60.96% ingresaron a la página de ofertas.
* El 49.56% ingresaron a la página del carrito.
* Finalmente, el 46.97% completó el pago.

No obstante, las acciones no siempre ocurren en la secuencia esperada. Al ordenar los datos por usuario y evento, se observó que la gran mayoría no sigue el orden esperado, ya que algunos pasan directamente de la página principal al carrito o a la compra. Para calcular de manera precisa cuántos usuarios cumplen con las etapas establecidas, se analizó una secuencia de pasos y se identificó en qué etapa se pierden más usuarios:

* Visitantes iniciales: 7,419.
* Vió página de ofertas: 4,593 usuarios iniciales / 4,201 usuarios que continuaron / 392 usuarios perdidos.
* Agregó un producto al carrito: 3,734 usuarios iniciales / 1,767 usuarios que continuaron / 1,967 usuarios perdidos.
* Pagó: 3,539 usuarios iniciales / 454 usuarios que continuaron / 3,085 usuarios perdidos.
* Vió Tutorial: 840 usuarios iniciales / 1 usuario que continuó / 839 usuarios perdidos.

Por último, se comprobó si existía una diferencia entre las proporciones de las muestras de los dos grupos de control a partir del total de usuarios y el número de casos de éxito. Se calculó el puntaje Z, obteniendo un p-value de 0.14 con un nivel de significancia de 0.05. Esto indica que no se puede rechazar la hipótesis nula, por lo que no hay razones para pensar que las proporciones son diferentes.

Asimismo, se compararon los dos grupos de control con el grupo experimental aplicando una prueba U de Mann-Whitney. En cada comparación se obtuvo un valor p de 1.0, lo que indica que no se puede rechazar la hipótesis nula; es decir, no existen diferencias en la distribución de los grupos.

Para finalizar, se calculó la corrección de Bonferroni, que ajusta el nivel de significancia original (α = 0.05) a 0.0167 al dividirlo entre el número de comparaciones (3). Con este nivel ajustado, cualquier valor p menor a 0.0167 indicaría una diferencia estadísticamente significativa entre los grupos. Sin embargo, al observar los resultados de las comparaciones, los valores p obtenidos son superiores al α ajustado, lo que sugiere que no hay suficiente evidencia para rechazar la hipótesis nula en ninguna de las comparaciones.

En conclusión, los resultados sugieren que los tres grupos (246, 247 y 248) tienen distribuciones muy similares en cuanto al número de usuarios únicos que realizaron cada evento, lo cual es consistente con una correcta asignación de los grupos en el experimento.

### Enlace al proyecto: [Haz click aquí](https://github.com/Hectorcidps/Portfolio_DA/blob/master/Proyecto%208%20-%20Comportamiento%20del%20usuario%20en%20una%20app%20de%20productos/comportamiento%20del%20usuario.ipynb)

# Proyecto 9 - Gimnasio Model Fitness

## Descripción: 
El objetivo del proyecto es analizar el comportamiento de los clientes de Model Fitness para desarrollar una estrategia basada en datos que reduzca la pérdida de usuarios. Este problema es especialmente crítico en el sector de gimnasios, donde identificar clientes que han dejado de utilizar el servicio puede ser desafiante, ya que algunos simplemente disminuyen su frecuencia de visitas antes de abandonarlo por completo.

Se realizó un análisis de los perfiles digitalizados de los clientes para identificar patrones de uso y desarrollar indicadores claros de pérdida, como la ausencia de visitas durante un mes. Basándonos en estos hallazgos, se diseñará una estrategia que permita identificar clientes en riesgo y proponer acciones para mejorar la retención.

## Características Principales: 

* Análisis exploratorio de los datos
* Cálculo de la tasa de retención
* Cálculo de la tasa de cancelación
* Correlación entre las características y la variable objetivo (cancelación)
* Construcción de modelo de regresión logística binaria
* Construcción de modelo Random Forest
* Evaluación de métricas sobre el rendimiento de los modelos
* Creación e identificación de clústeres de la variable objetivo

## Resultados: 
En conclusion el gimnasio cuenta con 2 grupos leales, los cuales representan a los usuarios mas comprometidos y activos. Es importante mantenerlos satisfechos para garantizar su continuidad. Por lo cual lanzar una campaña que recompense su lealtad podria ser una buena estrategia para seguir teniendo una buena respuesta por parte de estos grupos. 

Por ejemplo para el cluster 3 (3.9% - tasa de cancelacion) podria implementarse un programa de recompensas por su alta frecuencia de visitas, por ejemplo, ofrecer descuentos exclusivos, accesos prioritarios o membresias premium. Otra estrategia podria ser embajadores de marca, donde se les invite a programas de referidos para atraer nuevos clientes, por ejemplo, ofrecer una mensualidad por cada amigo referido que se inscriba. 

Para el cluster 1 (9.2% - tasa de cancelacion) el objetivo tendra que ser consolidar su lealtad y aumentar su compromiso con los servicios adicionales. Ofrecen promociones por tiempo limitado que refuercen el uso continuo del servicio, por ejemplo, pagar una cantidad de meses y obtener un descuento preferencial en el siguiente mes. Campaña de comunicación personalizada, enviar mensajes de agradecimiento o recordatorios para mantenerlos involucrados. 

Para los clusters 0 y 2 (27.4%, 30.2% - tasa cancelacion) el objetivo podria ser: mejorar su frecuencia de visitas y fortalecer su compromiso con la marca. Implementar encuestas de satisfaccion para entender que podria mejorar su experiencia, por ejemplo, responde la siguiente encuesta y gana una visita gratis. Implementar campaña de promociones dirigidas, ofrecer promociones atractivas basadas en su comportamiento de uso, por ejemplo, 30% de descuento en tu siguiente mensualidad si invitas a un amigo. 

Por otra parte para el cluster 4 (50.3% - tasa de cancelacion) el objetivo se centrara en estrategias intensivas de retencion, lanzar campañas especificas con descuentos significativos, por ejemplo, invitarlos a mantenerse en el gimnasio y ganar un 50% de descuento en su proxima mensualidad. Implementar beneficios del servicio con testimonios y estadísticas, por ejemplo, "El 80% de nuestros miembros notan mejoras significativas en 3 meses. ¡Tú puedes ser el próximo!”. Permitir pausas temporales o reembolsos parciales, por ejemplo, "Pausa tu membresia por un mes sin costo, y regresa cuando estes listo". 

Estas estrategias por cluster podrian maximizar las campañas de marketing al abordar las necesidades y comportamientos unicos de cada grupo. 


## 🛠️ Tecnologías implementadas
* Lenguajes de Programación: Python
* Librería de limpieza y manipulación de datos: Pandas
* Librerias de visualización: Matplotlib, Seaborn
* Librería de Machine Lerarning: Scikit

## 📈 Competencias
* Limpieza y Preparación de Datos
* Visualizacion de graficos
* Entrenamiento de modelos de aprendizaje automático
# Proyecto Final - Telecomunicaciones: Identificar operadores ineficaces

##  Descripción: 
El servicio de telefonía virtual CallMeMaybe está desarrollando una nueva función que brindará a los supervisores y las supervisores información sobre los operadores menos eficaces. Se considera que un operador es ineficaz si tiene una gran cantidad de llamadas entrantes perdidas (internas y externas) y un tiempo de espera prolongado para las llamadas entrantes. Además, si se supone que un operador debe realizar llamadas salientes, un número reducido de ellas también será un signo de ineficacia.

Los datasets contienen información sobre el uso del servicio de telefonía virtual CallMeMaybe. Sus clientes son organizaciones que necesitan distribuir gran cantidad de llamadas entrantes entre varios operadores, o realizar llamadas salientes a través de sus operadores. Los operadores también pueden realizar llamadas internas para comunicarse entre ellos. Estas llamadas se realizan a través de la red de CallMeMaybe.

## 🛠️ Tecnologías implementadas
* Lenguajes de Programación: Python
* Librería de limpieza y manipulación de datos: Pandas, NumPy, Math, Datetime
* Librerias de visualización: Matplotlib, Seaborn
* Librerias de pruebas estadísticas: SciPy, Stats

## 📈 Competencias
* Limpieza y Preparación de Datos
* Visualizacion de gráficos
* Análisis de embudo de eventos
* Pruebas A/B
* Comprobación de hipótesis 

## Características Principales: 

### El enfoque para analizar e identificar a los operadores menos eficaces fue diseñado completamente por mí, implementando las siguientes acciones:

* Analisis exploratorio de los datos, enfocado en encontrar valores ausentes, duplicados y valores atipicos
* Calcular el peso de los valores ausentes dentro de los dataSets 
* Enriquecer los datos, agregando columnas con datos separados en meses, semanas, días. 
* Distribución de llamadas entrantes y salientes por día, semana y mes.
* Distribución de llamadas entrantes y salientes por operador, por día, semana y mes.
* Calcular el número de llamadas entrantes y salientes por operador.
* Calcular el índice de ineficacia de operadores.
* Identificar operadores por tipo de plan.
* Cálculo de métricas relevantes por tipo de plan.
* Identificar operadores ineficaces por plan.
* Prueba de hipótesis estadísticas.

#### Hipótesis estadísticas propuestas: 
1. Comparación entre los tiempos de espera de los planes tarifarios.

* Hipótesis Nula: No existen diferencias significativas entre los tiempos de espera de los distintos planes.
* Hipótesis Alternativa: Existen diferencias significativas (al menos en una) entre los tiempos de espera de los distintos planes.

2. Diferencia entre el tiempo de espera promedio de operadores más eficaces y menos eficaces.

* Hipótesis Nula: No existen diferencias significativas en el tiempo de espera promedio entre los operadores más eficaces y los menos eficaces.
* Hipótesis Alternativa: Existen diferencias significativas en el tiempo de espera promedio entre los operadores más eficaces de los menos eficaces.

3. Tiempo promedio de operadores con más llamadas perdidas y menos llamadas perdidas.

* Hipótesis nula: No hay diferencias significativas en el tiempo promedio de espera entre operadores con más y menos llamadas perdidas.
* Hipótesis alternativa: Hay diferencias significativas en el tiempo promedio de espera entre operadores con más y menos llamadas perdidas.


## Resultados:
Durante el análisis de eficiencia operativa en llamadas, se identificaron 4900 valores duplicados que coincidían en el user_id y la fecha de recuperación de datos. Aunque inicialmente se consideraron para eliminación, se determinó que eran relevantes para el análisis y se mantuvieron. En cuanto a los valores ausentes, se encontraron 117 registros en la columna internal, asociados mayoritariamente a llamadas entrantes posiblemente no atendidas. Por otro lado, en la columna operator_id, los 8289 valores ausentes representaban el 15% del total de datos y correspondían principalmente a llamadas perdidas o salientes sin asignar a un operador. Estas observaciones reafirmaron la importancia de conservar esta información para un análisis más detallado.

El análisis exploratorio reveló patrones interesantes en la distribución de las llamadas. Gráficos mostraron que las llamadas salientes predominaban y que las semanas 40 a 45 registraron un aumento notable en la actividad de los operadores, aunque solo unos pocos lograron superar las 8000 llamadas, y uno alcanzó las 10,000. Al evaluar las diferencias entre direcciones, se observó un mayor volumen de llamadas salientes en comparación con las entrantes, mientras que la cantidad de llamadas perdidas se mantuvo baja y equilibrada entre ambos tipos.

Para medir la ineficiencia operativa, se desarrolló un índice considerando tres métricas clave: el promedio de llamadas perdidas, el tiempo de espera y el número de llamadas salientes por operador. Este análisis destacó al operador con el mayor índice de ineficacia, quien registró un 2% de llamadas perdidas, un promedio de 17 minutos de espera y un bajo porcentaje de llamadas salientes. Con base en percentiles, se segmentaron los operadores en tres grupos. El Grupo A, con un 31% de ineficiencia y un tiempo de espera promedio de 457 minutos, mostró los peores resultados. El Grupo C, en cambio, fue el más eficiente, con solo un 20% de ineficiencia y un tiempo de espera promedio de 137 minutos.

Para confirmar estas diferencias, se realizaron pruebas estadísticas. La prueba de Kruskal-Wallis indicó diferencias significativas en los tiempos de espera promedio entre los grupos. Además, la prueba U de Mann-Whitney confirmó diferencias estadísticamente significativas entre operadores más y menos eficaces en términos de tiempo de espera. Una evaluación adicional de las llamadas perdidas, utilizando percentiles para segmentarlas, evidenció también una distribución no normal. La prueba U de Mann-Whitney validó que existe una diferencia significativa en el tiempo promedio de los operadores con más y menos llamadas perdidas.

### Enlace al proyecto: [Haz click aquí](https://github.com/Hectorcidps/Portfolio_DA/blob/master/Proyecto%20final/Proyecto%20Telecomunicaciones/Telecomunicaciones.ipynb)
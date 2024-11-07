import requests
import pandas as pd 
from bs4 import BeautifulSoup

URL = 'https://practicum-content.s3.us-west-1.amazonaws.com/data-analyst-eng/moved_chicago_weather_2017.html'

df = requests.get(URL)
soup = BeautifulSoup(df.text, 'lxml')

tabla = soup.find('table', attrs={'id' : 'weather_records'})

# encabezados
encabezados = []
for row in tabla.find_all('th'):
    encabezados.append(row.text)
# contenido
contenido = []
for fila in tabla.find_all('tr'):
    if not fila.find_all('th'):
        contenido.append([element.text for element in fila.find_all('td')])

# construir DF
weather_records = pd.DataFrame(contenido, columns=encabezados)
print(weather_records)
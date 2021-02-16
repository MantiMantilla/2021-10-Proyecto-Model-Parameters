import requests as rq
import pandas as pd

url = 'https://copa-uniandes.github.io/2021-10-Proyecto-Model-Parameters/'
html = rq.get(url).content
df_list = pd.read_html(html)
ranking = df_list[0]
print(ranking)
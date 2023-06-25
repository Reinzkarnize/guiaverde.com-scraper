from bs4 import BeautifulSoup
import requests
import json
import pandas as pd

total_page = 69

url = 'https://www.guiaverde.com/empresas/buscar/frutos-rojos-berries/null/0/0/'

req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

with open('raw/res.html', 'w') as file:
    file.write(req.text)

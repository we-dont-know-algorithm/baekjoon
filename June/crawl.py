
import requests
from bs4 import BeautifulSoup
import json
import os

# python파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

req = requests.get('https://www.acmicpc.net/step/10')
html = req.text
soup = BeautifulSoup(html, 'html.parser')

list = soup.select(
    '#problemset > tbody > tr > td.click-this > a'
)

for item in list:
    link = "https://www.acmicpc.net"
    print(item.text)
    print(link + item['href'])

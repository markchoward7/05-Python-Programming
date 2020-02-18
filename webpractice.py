import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.python.org/')
bsh = BeautifulSoup(html.read(), 'html.parser')
print(bsh.title)
print(bsh.h1)
print(bsh.h2)
print(bsh.h3)

r = requests.get('https://analytics.usa.gov/data/live/realtime.json').json()
print(r['data'][0])

r = urlopen('http://www.py4inf.com/code/romeo-full.txt').read()
print(len(r))
print(r[:3000])
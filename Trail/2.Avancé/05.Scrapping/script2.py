from bs4 import BeautifulSoup
from lxml import etree
import requests

# Url of website
url='https://medi-market.be/fr/antirides-anti-age/c/2253'
r = requests.get(url)
soup = BeautifulSoup(r.content,'lxml')

# for p in soup.find_all('h1'):
#     print (p.text)
file = open('medimarket.html',"w")
file.write(soup.prettify())
file.close()


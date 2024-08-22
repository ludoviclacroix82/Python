from bs4 import BeautifulSoup
from lxml import etree
import requests
# file = open("../data/data.xml", "r")
# print (file.read())
# file.close()



# tree = etree.parse("../data/data.xml")

# for user in tree.xpath("/users/user/nom"):
#     print(user.text)
    

# tree = etree.parse("../data/data.xml")
# for user in tree.xpath("/users/user"):
#     print(user.get("data-id"))
    
# tree = etree.parse("../data/data.xml")
# for user in tree.xpath("/users/user[metier='Veterinaire']/nom"):

#     print(user.text)

# file = open("../data/becode.html", "r")
# #print(fichier.read())
# html_doc=file.read()
# file.close()
# html_doc


# soup = BeautifulSoup(html_doc, "lxml")
# # In my file (becode.org) by looking at this html script We can see that the main title is arranged in the h1 tag

# for p in soup.find_all('h1'):
#     # We only retrieve the content ==> .text
#     print (p.text)
# for p in soup.find('h2'):
#     # We only retrieve the content ==> .text
#     print (p.text)
# for p in soup.find_all('p'):
#     # We only retrieve the content ==> .text
#     print (p.text)


# Url of website
url='https://www.becode.org/about/'
# I send my HTTP request with a "GET" to the site server to identify in the url
r = requests.get(url)
# I display the requested url and the return of the server
# I ask beautifulSoup to keep in a soup variable the web page to scrape (url) an html script
soup = BeautifulSoup(r.content,'lxml')

for p in soup.find_all('h1'):
    # We only retrieve the content ==> .text
    print (p.text)
for p in soup.find_all('h2'):
    # We only retrieve the content ==> .text
    print (p.text)
for p in soup.find_all('p'):
    # We only retrieve the content ==> .text
    print (p.text)
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import csv

#-------------------------------------------<<< TWITTER >>>-------------------------------------------

mi_url = "https://twitter.com/espol"
uClient = uReq(mi_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

filename = "datos.csv"
f = open(filename, "w")

#palabras_clave = ['curso', 'taller', 'seminario', 'maestría', 'participa']

contenedores = page_soup.findAll("div", {"class": "tweet"})

for contenedor in contenedores:
    tweet_contenedor = contenedor.findAll("div", {"class":"js-tweet-text-container"})
    tema = tweet_contenedor[0].text.strip()
    enlace = "https://twitter.com" + contenedor['data-permalink-path']

    #---<<< filtro anti emoji >>>---
    tema_valido = ''
    for letra in tema:
        if (31 < ord(letra) < 255):
            tema_valido = tema_valido + letra
     #---<<< filtro anti emoji >>>---

    #for palabra in palabras_clave:
    #    if (tema_valido.find(palabra) != -1):
    #        f.write(tema_valido + "," +  enlace + "\n")
    #        break
        
    f.write("\"" + tema_valido + "\"" + "," + "\"" + enlace + "\"" + "\n")

print ('<<<<< TWITTER >>>>>')
f.close()
#-------------------------------------------<<< TWITTER >>>-------------------------------------------
#-------------------------------------------<<< FACEBOOK >>>-------------------------------------------

'''
mi_url = "https://www.facebook.com/espol/"
uClient = uReq(mi_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

posts = page_soup.findAll("div", {"class": "_5pbx userContent _3576"})

for post in posts:
    resultado = post.findAll("p")
    tema = resultado[0].text.strip()
    link = post.findAll("a")[0].text

    #---<<< filtro anti emoji >>>---
    tema_valido = ''
    for letra in tema:
        if (31 < ord(letra) < 255):
            tema_valido = tema_valido + letra
    #---<<< filtro anti emoji >>>---

    for palabra in palabras_clave:
        if (tema_valido.find(palabra) != -1):
            f.write(tema_valido + ',' + link + "\n")
            break

f.close()
print ('<<<< FACEBOOK >>>')
'''

#-------------------------------------------<<< FACEBOOK >>>-------------------------------------------
#-------------------------------------------<<< INSTAGRAM >>>-------------------------------------------
#-------------------------------------------<<< INSTAGRAM >>>-------------------------------------------
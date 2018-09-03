from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import csv

mi_url = "https://www.twitter.com/espol"

uClient = uReq(mi_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

filename = "datos_twitter.csv"
f = open(filename, "w")

headers = "contenido, enlace\n"
f.write(headers)

palabras_clave = ['curso', 'taller', 'seminario', 'maestría', 'participa']

contenedores = page_soup.findAll("div", {"class": "tweet"})

for contenedor in contenedores:
    tweet_contenedor = contenedor.findAll("div", {"class":"js-tweet-text-container"})
    tema = tweet_contenedor[0].text.strip()
    enlace = "https://twitter.com" + contenedor['data-permalink-path']

    #---<<< filtro anti emoji >>>---
    tema_valido = ''
    for letra in tema:
        if (1 < ord(letra) < 255):
            tema_valido = tema_valido + letra
     #---<<< filtro anti emoji >>>---
    
    for palabra in palabras_clave:
        if (tema_valido.find(palabra) != -1):
            f.write(tema_valido + "," +  enlace + "\n")
            break

f.close()
print ('<<<<<>>>>>')
print ('<<<<FIN>>>')
print ('<<<<<>>>>>')
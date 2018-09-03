from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import csv

mi_url = "https://www.facebook.com/espol/"

uClient = uReq(mi_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

filename = "datos_facebook.csv"
f = open(filename, "w")

headers = "contenido, enlace\n"
f.write(headers)

palabras_clave = ['curso', 'taller', 'seminario', 'maestría', 'participa']

posts = page_soup.findAll("div", {"class": "_5pbx userContent _3576"})

for post in posts:
    resultado = post.findAll("p")
    tema = resultado[0].text.strip()

    #---<<< filtro anti emoji >>>---
    tema_valido = ''
    for letra in tema:
        if (31 < ord(letra) < 255):
            tema_valido = tema_valido + letra
     #---<<< filtro anti emoji >>>---

    link = post.findAll("a")[0].text

    for palabra in palabras_clave:
        if (tema_valido.find(palabra) != -1):
            #resultado = "Descripción: " + str(tema_valido) + "\nLink: " + str(link) + "\n"
            #print(resultado)
            f.write(tema_valido + ',' + link + "\n")
            break

f.close()
print ('<<<<<>>>>>')
print ('<<<<FIN>>>')
print ('<<<<<>>>>>')
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import json, time, re
#import csv

#-------------------------------------------<<< TWITTER >>>-------------------------------------------

mi_url = "https://twitter.com/espol"
uClient = uReq(mi_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

filename = "datos.txt"
f = open(filename, "w")

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
        
    f.write(tema_valido + "\n")
    f.write(enlace + "\n")

print ('<<<<< TWITTER >>>>>')
#f.close()
#-------------------------------------------<<< TWITTER >>>-------------------------------------------
#-------------------------------------------<<< FACEBOOK >>>-------------------------------------------

mi_url = "https://www.facebook.com/espol/"
uClient = uReq(mi_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

posts = page_soup.findAll("div", {"class": "_1dwg _1w_m _q7o"})

for post in posts:
    resultado = post.findAll("p")
    tema = resultado[0].text.strip()
    #link = post.findAll("a")[0].text.strip()
    link = "https://www.facebook.com/pg/espol/posts/?ref=page_internal"

    #---<<< filtro anti emoji >>>---
    tema_valido = ''
    for letra in tema:
        if (31 < ord(letra) < 255):
            tema_valido = tema_valido + letra
    #---<<< filtro anti emoji >>>---

    #for palabra in palabras_clave:
    #    if (tema_valido.find(palabra) != -1):
    #        f.write(tema_valido + ',' + link + "\n")
    #        break

    f.write(tema_valido + "\n")
    f.write(link + "\n")

#f.close()
print ('<<<< FACEBOOK >>>')


#-------------------------------------------<<< FACEBOOK >>>-------------------------------------------
#-------------------------------------------<<< INSTAGRAM >>>-------------------------------------------

mi_url = "https://www.instagram.com/espol1/"

uClient = uReq(mi_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

script_tag = page_soup.find('script',text=re.compile('window\._sharedData'))
shared_data = script_tag.string.partition('=')[-1].strip(' ;')
result = json.loads(shared_data)
n = len(result['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges'])
for i in range(1,n):
    descripcion = result['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['edge_media_to_caption']['edges'][0]['node']['text']
    enlace = result['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['display_url']
    #print(descripcion)
    #print(enlace)

    #---<<< filtro anti emoji >>>---
    tema_valido = ''
    for letra in descripcion:
        if (31 < ord(letra) < 255):
            tema_valido = tema_valido + letra
    #---<<< filtro anti emoji >>>---

    f.write(tema_valido + "\n")
    f.write(enlace + "\n")

f.close()
print ('<<<< INSTAGRAM >>>')

#-------------------------------------------<<< INSTAGRAM >>>-------------------------------------------
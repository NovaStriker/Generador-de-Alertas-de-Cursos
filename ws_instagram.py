from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import csv
import json, time, re
mi_url = "https://www.instagram.com/espol1/"

uClient = uReq(mi_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")


#filename = "alertaInstagram.csv"
#f = open(filename, "w")
#headers = "Tema: \nLink: \n"
#f.write(headers)
#posts = page_soup.findAll("body")
script_tag = page_soup.find('script',text=re.compile('window\._sharedData'))
shared_data = script_tag.string.partition('=')[-1].strip(' ;')
result = json.loads(shared_data)
n = len(result['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges'])
for i in range(1,n):
    resultado = "Descripcion: " +result['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['edge_media_to_caption']['edges'][0]['node']['text'] + "\nImagen: " + result['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['display_url']+"\n"
    print(resultado)




#f.close()

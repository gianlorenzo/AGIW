import json
import urllib.request
from urllib.request import (urlretrieve,urlunparse,urlparse)
import urllib.error
from bs4 import BeautifulSoup
import requests
from urllib import error
import cssutils

import os
from cssselect import GenericTranslator, SelectorError

import cssutils
#Legge file .json. Ritorna un dizionario con {nome sito web, array di url}
def readJson():
    return json.load(open('/home/gianlorenzo/AGIW/dexter_urls_category_notebook.json'))

#Ritorna tutte le chiavi del dizionario
def takeAllKeys():
   return list(readJson())

#Urllib è una libreria python che fornisce un'interfaccia con il world wide web. La sua funzione urlopen()
#accetta in input la URL di un sito web e ritorna la pagine web stessa il cui codice viene letto attraverso la funzione read()
#BeautifulSoup prende come argomento un codice HTML e restituisce un oggetto BeautifulXoup come una
#struttura dati annidata costituente l'intero codice html della pagine web, compresi css ed immagini
def takeHtmlContent(url):
    request = urllib.request.Request(url)
    result = urllib.request.urlopen(request)
    resultText = result.read()
    soup = BeautifulSoup(resultText,"lxml")
    return soup

def writeHtmlFile(url):
    try:
        r = takeHtmlContent(url)
    except urllib.error.URLError as e:
        f = open("error.txt","w+")
        f.write("porcaeva")
        f.close()
    else:
        f = open("noError.html","w+")
        f.write(str(r))
        f.close()
    return f

urlBuona = "https://www.ecrater.com/p/2042546/toshiba-satellite-a40-series-recovery"
urlCattiva = "http://53laptop.com/product/505_hp+touchsmart+tx2+121+inch+notebook"

def takeCss(url):
    r = takeHtmlContent(url)
    css_url = [link["href"] for link in r.findAll("link") if "stylesheet" in link.get("rel",[])]
    for x in css_url:
        y = x.split('/',-1)[-1]
        outpath = os.path.join("css",y)
        urlretrieve(x,outpath)

def takeImage(url):
    parsed = list(urlparse(url))
    soup = takeHtmlContent(url)
    for image in soup.find_all("img"):
        # print("Image: %(src)s" % image)
        filename = image["src"].split("/")[-1]
        # print(image["src"])
        parsed[2] = image["src"]
        outpath = os.path.join("immagini", filename)
        if image["src"].lower().startswith("http"):
            urlretrieve(image["src"], outpath)
        else:
            urlretrieve(urlunparse(parsed), outpath)



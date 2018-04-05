import json
import urllib.request
import urllib.error
import urllib.parse
from bs4 import BeautifulSoup
import os


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
def openUrl(url):
    request = urllib.request.Request(url)
    result = urllib.request.urlopen(request)
    resultText = result.read()
    return resultText


def writeAllFile():
    keys = takeAllKeys()
    os.makedirs("notebook")
    for key in keys:
        os.makedirs("/home/gianlorenzo/PycharmProjects/AGIW/TakeUrls/notebook/"+str(key))
        index = open("/home/gianlorenzo/PycharmProjects/AGIW/TakeUrls/notebook/"+str(key)+"/"+"index.txt","w+")
        i=1
        for value in readJson()[key]:
            try:
                soup = takeHtmlContent(value)
            except urllib.request.URLError as e:
                index.write(str(value)+"\t"+str(e.reason)+"\n")
            except urllib.request.HTTPError as e:
                index.write(str(value)+"\t"+str(e.code)+"\n")
            else:
                index.write(str(value)+"\t"+str(i)+".html"+"\n")
                html = open("/home/gianlorenzo/PycharmProjects/AGIW/TakeUrls/notebook/"+str(key)+"/"+str(i)+".html","w+")
                html.write(str(soup))
                html.close()
            i = i+1
        index.close()


writeAllFile()





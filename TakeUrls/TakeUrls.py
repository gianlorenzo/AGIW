import json
import urllib.request
import urllib.error
import urllib.parse
from bs4 import BeautifulSoup
import os
import logging
import sys
from datetime import datetime

#Legge file .json. Ritorna un dizionario con {nome sito web, array di url}
def readJson():
    return json.load(open('/home/davben/AGIW/dexter_urls_category_notebook.json'))

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
    log = open("writeAllFile.log","a")
    sys.stdout = log
    print("start "+datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    logging.warn("start "+datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    keys = takeAllKeys()
    print("prese le chiavi..")
    os.makedirs("notebook")
    print("creata dir notebook")
    logging.warn("creata dir notebook")
    for key in keys:
        logging.warn("creo cartella: "+str(key))
        os.makedirs("/home/davben/git/AGIW-master/AGIW/TakeUrls/notebook/"+str(key))
        print("creata dir: "+str(key)+"..")
        index = open("/home/davben/git/AGIW-master/AGIW/TakeUrls/notebook/"+str(key)+"/"+"index.txt","w+")
        print("creato file index ..")
        i=1
        print("leggo lista di html in chiave: "+str(key)+"..")
        for value in readJson()[key]:
            try:
                soup = takeHtmlContent(value)
                print("prendo HtmlContent di "+str(value)+"..")
            except urllib.request.URLError as e:
                index.write(str(value)+"\t"+str(e.reason)+"\n")
                logging.warn("non scrivo " + str(i) + ".html" + " in " + str(key))
            except urllib.request.HTTPError as e:
                index.write(str(value)+"\t"+str(e.code)+"\n")
                logging.warn("non scrivo " + str(i) + ".html" + " in " + str(key))
            else:
                index.write(str(value)+"\t"+str(i)+".html"+"\n")
                print("scrivo "+str(i)+".html"+" in "+str(key))
                logging.warn("scrivo "+str(i)+".html"+" in "+str(key))
                html = open("/home/davben/git/AGIW-master/AGIW/TakeUrls/notebook/"+str(key)+"/"+str(i)+".html","w+")
                html.write(str(soup))
                html.close()
            i = i+1
        logging.warn(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+ " fine scrittura degli html in "+str(key))
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+ " fine scrittura degli html in "+str(key))
        logging.warn("ho letto: "+str(i)+" pagine html..")
        print("finita scrittura di index della cartella: "+str(key))
        index.close()
    logging.warn("fine "+datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print("fine "+datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


writeAllFile()





import json

import urllib.request
import urllib.error
import urllib.parse
from bs4 import BeautifulSoup
import os
import sys
import logging
from datetime import datetime
import http.client
from socket import error as SocketError

pathJsonFile = '/home/gianlorenzo/AGIW/dexter_urls_category_notebook.json'
dirOutput = '/home/gianlorenzo/AGIW/'
dirOutputNotebook = '/home/gianlorenzo/AGIW/notebook/'


#Legge file .json. Ritorna un dizionario con {nome sito web, array di url}
def readJson():
    return json.load(open(pathJsonFile))

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
    soup = BeautifulSoup(result.read(),"lxml")
    return soup

def downloadHtmlFile():
    log = open("writeAllFile.log", "a")
    sys.stdout = log
    print("start "+datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    logging.warning("start "+datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    keys = takeAllKeys()
    os.makedirs(dirOutput+"notebook")
    logging.warning("creata dir notebook")
    for key in keys:
        logging.warning("creo cartella: " + str(key))
        os.makedirs(dirOutputNotebook+str(key))
        print("creata dir: " + str(key) + "..")
        index = open(dirOutputNotebook+str(key)+"/"+"index.txt","w+")
        i=1
        print("leggo lista di html in chiave: "+str(key)+"..")
        for value in readJson()[key]:
            try:
                soup = takeHtmlContent(value)
                print("prendo HtmlContent di "+str(value)+"..")
            except urllib.request.URLError as e:
                index.write(str(value)+"\t"+str(e.reason)+"\n")
                logging.warning("non scrivo " + str(i) + ".html" + " in " + str(key))
            except urllib.request.HTTPError as e:
                index.write(str(value)+"\t"+str(e.reason)+"\n")
                logging.warning("non scrivo " + str(i) + ".html" + " in " + str(key))
            except urllib.request.ContentTooShortError as e:
                index.write(str(value) + "\t" + str(e.reason) + "\n")
                logging.warning("non scrivo " + str(i) + ".html" + " in " + str(key))
            except http.client.HTTPException:
                index.write(str(value) + "\t" + "HTTPException" + "\n")
                logging.warning("non scrivo " + str(i) + ".html" + " in " + str(key))
            except SocketError:
                index.write(str(value) + "\t" + "HTTPException" + "\n")
                logging.warning("non scrivo " + str(i) + ".html" + " in " + str(key))
            else:
                index.write(str(value)+"\t"+str(i)+".html"+"\n")
                print("scrivo "+str(i)+".html"+" in "+str(key))
                html = open(dirOutputNotebook+str(key)+"/"+str(i)+".html","w+")
                html.write(str(soup))
                html.close()
            i = i+1
            logging.warning(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " fine scrittura degli html in " + str(key))
            print(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " fine scrittura degli html in " + str(key))
            logging.warning("ho letto: " + str(i) + " pagine html..")
            print("finita scrittura di index della cartella: " + str(key))
        index.close()
        logging.warning("fine " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        print("fine " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))




writeAllFile()
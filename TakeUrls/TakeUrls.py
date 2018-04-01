import json
from pprint import pprint

#Legge file .json. Ritorna un dizionario con {nome sito web, array di url}
def readJson():
    return json.load(open('/home/gianlorenzo/AGIW/dexter_urls_category_notebook.json'))

#Scrive in un array tutte le chiavi del dizionario
def takeAllKeys():
    keys = []
    for i in readJson():
        keys.append(i)
    return keys



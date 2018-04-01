import json

#Legge file .json. Ritorna un dizionario con {nome sito web, array di url}
def readJson():
    return json.load(open('/home/gianlorenzo/AGIW/dexter_urls_category_notebook.json'))

#Ritorna tutte le chiavi del dizionario
def takeAllKeys():
   return list(readJson())



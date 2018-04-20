import json
import os
import shutil

def readJson():
    return json.load(open('/home/gianlorenzo/AGIW/dexter_urls_category_notebook.json'))

def takeAllKeys():
   return list(readJson())

def checkDir(dir):
    # print(len([name for name in os.listdir(dir) if os.path.isfile(os.path.join(dir, name))]))
    return (len(os.listdir(dir)))

# Ritorna numero cartelle e url totali
def getNumbersOfDataset():
    print ("Numero cartelle :" + str(len(readJson().keys())))
    i = 0
    for key in takeAllKeys():
        for value in readJson()[key]:
            i = i+1
    print ("Numero pagine: "+ str(i))

# Ritorna numero cartelle per le quali funziona almeno una url
def getNumberOfOneUrl():
    listadir = os.listdir("/media/gianlorenzo/UBUNTU 17_1/notebook/")
    i = 0
    for dir in listadir:
        if not checkDir("/media/gianlorenzo/UBUNTU 17_1/notebook/"+dir)==1:
            i = i+1
    print("Numero cartelle per le quali funziona almeno una url: "+str(i))

# Ritorna numero url funzionanti:
def getTotalUrlOk():
    listadir = os.listdir("/media/gianlorenzo/UBUNTU 17_1/notebook/")
    i = 0
    for dir in listadir:
        if not checkDir("/media/gianlorenzo/UBUNTU 17_1/notebook/" + dir) == 1:
            listaFile = os.listdir("/media/gianlorenzo/UBUNTU 17_1/notebook/" + dir)
            listaFile.remove("index.txt")
            for file in listaFile:
                i = i+1
    print("Numero url funzionanti: "+ str(i))


# Elimina le cartelle doppioni
def getDirOk():
    dire1 = "/home/gianlorenzo/AGIW/Step1/"
    dire2 = "/home/gianlorenzo/AGIW/notebook/"
    listaDir1 = os.listdir(dire1)
    listaDir2 = os.listdir(dire2)
    for dir1 in listaDir1:
        for dir2 in listaDir2:
            if dir2 in listaDir1:
                shutil.rmtree(dire2+dir2)

# Elimina le cartelle senza html
def removeDirWithNoHtml():
    listadir = os.listdir("/home/gianlorenzo/AGIW/notebook/")
    for dir in listadir:
        if checkDir("/home/gianlorenzo/AGIW/notebook/"+dir) == 1:
            shutil.rmtree("/home/gianlorenzo/AGIW/notebook/"+dir)


# Ritorna numero url che hanno prodotto json
def getNumberoOfJson():
    listaDir = os.listdir("/home/gianlorenzo/Scrivania/jsonFatti/")
    i = 0
    for dir in listaDir:
        if not checkDir("/home/gianlorenzo/Scrivania/jsonFatti/" + dir) == 1:
            listaFile = os.listdir("/home/gianlorenzo/Scrivania/jsonFatti/" + dir)
            for file in listaFile:
                f = open("/home/gianlorenzo/Scrivania/jsonFatti/" + dir + "/" + file)
                if not f.read() == "[]" and not f.read() == "[{}]":
                    i = i+1
    print("Numero totale di json non vuoti:" + str(i))


getNumberoOfJson()
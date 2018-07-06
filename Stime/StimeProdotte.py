import json
import os
import shutil
import sys

pathJsonFile = '/home/gianlorenzo/AGIW/dexter_urls_category_notebook.json'
dirOutputNotebook = '/home/gianlorenzo/AGIW/notebook/'
dirOutputJson = '/home/gianlorenzo/AGIW/FINALJSON/'

def readJson():
    return json.load(open(pathJsonFile))

def takeAllKeys():
   return list(readJson())


def checkDir(dir):
    # print(len([name for name in os.listdir(dir) if os.path.isfile(os.path.join(dir, name))]))
    return (len(os.listdir(dir)))

def checkDir(dir):
    # print(len([name for name in os.listdir(dir) if os.path.isfile(os.path.join(dir, name))]))
    return (len(os.listdir(dir)))

def getTotalDirectoryWithHtml(url):
    listaDir = os.listdir(url)

    len = 0
    numDir=0
    for dir in listaDir:
        len = len + checkDir(url+dir)
        numDir = numDir+1
    print(str(len))
    print(str(numDir))

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
    listadir = os.listdir(dirOutputNotebook)
    i = 0
    for dir in listadir:
        if not checkDir(dirOutputNotebook+dir)==1:
            i = i+1
    print("Numero cartelle per le quali funziona almeno una url: "+str(i))


# Ritorna numero url funzionanti:
def getTotalUrlOk():
    listadir = os.listdir(dirOutputNotebook)
    i = 0
    for dir in listadir:
        if not checkDir(dirOutputNotebook+ dir) == 1:
            listaFile = os.listdir(dirOutputNotebook+ dir)
            listaFile.remove("index.txt")
            for file in listaFile:
                i = i+1
    print("Numero url funzionanti: "+ str(i))
getTotalUrlOk()

# Elimina le cartelle doppioni
def getDirOk():
    listaDir1 = os.listdir(dirOutputJson)
    listaDir2 = os.listdir(dirOutputNotebook)
    for dir1 in listaDir1:
        for dir2 in listaDir2:
            if dir2 in listaDir1:
                shutil.rmtree(dirOutputNotebook+dir2)

# Elimina le cartelle senza html
def removeDirWithNoHtml():
    listadir = os.listdir(dirOutputNotebook)
    for dir in listadir:
        if checkDir(dirOutputNotebook+dir) == 1:
            shutil.rmtree(dirOutputNotebook+dir)

# Ritorna numero url che hanno prodotto json
def getNumberoOfJson():
    listaDir = os.listdir(dirOutputJson)
    listaDir.remove("writeLogJson.log")
    i = 0
    for dir in listaDir:
        if not checkDir(dirOutputJson + dir) == 1:
            listaSubDir = os.listdir(dirOutputJson + dir)
            for subDir in listaSubDir:
                listaFile = os.listdir(dirOutputJson + dir + "/" + subDir)
                for file in listaFile:
                    f = open(dirOutputJson + dir +"/"+subDir + "/" + file)
                    if not f.read()=="{}" or not f.read()=="{"": ""}" or not f.read()=="[]" or not f.read()=="[{}]" or not f.read()=="Features: []" :
                        i = i+1
    print("Numero totale di json non vuoti:" + str(i))

def checkFile():
    log = open("myLog.log","a")
    sys.stdout = log
    listaDir = os.listdir(dirOutputJson)
    listaDir.remove("writeLogJson.log")
    vuotiTotali = 0
    pieniTotali = 0
    for dir in listaDir:
        listaSubDir = os.listdir(dirOutputJson+dir)
        vuoto = 0
        pieno = 0
        for subDir in listaSubDir:

            listaFile = os.listdir(dirOutputJson+dir+"/"+subDir)

            for file in listaFile:
                f = open(dirOutputJson+dir+"/"+subDir+"/"+file)
                if f.read()=="{}" or f.read()=="{"": ""}" or f.read()=="[]" or f.read()=="[{}]" or f.read()=="Features: []" :
                    vuoto = vuoto + 1

                else:
                    pieno = pieno + 1
        pieniTotali = pieniTotali+pieno
        vuotiTotali = vuotiTotali+vuoto

        print("Nella cartella " + dir+" "+"ho un numero di file vuoti = a "+str(vuoto)+" e di file pieni = a "+str(pieno))
    print("File totali pieni: "+" "+str(pieniTotali)," File totali vuoti: "+str(vuotiTotali))

# Ritorna numero url che hanno prodotto json
def getNumberoOfJsonSPEXA():
    listaDir = os.listdir(dirOutputJson)
    i = 0
    for dir in listaDir:
        if not checkDir(dirOutputJson + dir) == 1:
            listaFile = os.listdir(dirOutputJson + dir)
            for file in listaFile:
                f = open(dirOutputJson + dir + "/" + file)
                if not f.read() == "[]" and not f.read() == "[{}]":
                    i = i+1
    print("Numero totale di json non vuoti:" + str(i))

def checkFileSPEXA():
    log = open("myLog.log","a")
    sys.stdout = log
    listaDir = os.listdir(dirOutputJson)
    vuotiTotali = 0
    pieniTotali = 0
    for dir in listaDir:
        listaFile = os.listdir(dirOutputJson+dir)
        vuoto = 0
        pieno = 0
        for file in listaFile:
            f = open(dirOutputJson+dir+"/"+file)
            if f.read()=="[]" or f.read()=="[{}]":
                vuoto = vuoto + 1

            else:
                pieno = pieno + 1
        pieniTotali = pieniTotali+pieno
        vuotiTotali = vuotiTotali+vuoto

        print("Nella cartella "+dir+"ho un numero di file vuoti = a "+str(vuoto)+" e di file pieni = a "+str(pieno))
    print(str(pieniTotali),str(vuotiTotali))


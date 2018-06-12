import os
import logging
import sys
def checkFile():
    log = open("myLog.log","a")
    sys.stdout = log
    listaDir = os.listdir("/home/gianlorenzo/AGIW/JSONSTEP1(4)/")
    vuotiTotali = 0
    pieniTotali = 0
    for dir in listaDir:
        listaFile = os.listdir("/home/gianlorenzo/AGIW/JSONSTEP1(4)/"+dir)
        vuoto = 0
        pieno = 0
        for file in listaFile:
            f = open("/home/gianlorenzo/AGIW/JSONSTEP1(4)/"+dir+"/"+file)
            if f.read()=="{}" or f.read()=="{"": ""}":
                vuoto = vuoto + 1

            else:
                pieno = pieno + 1
        pieniTotali = pieniTotali+pieno
        vuotiTotali = vuotiTotali+vuoto

        print("Nella cartella "+dir+"ho un numero di file vuoti = a "+str(vuoto)+" e di file pieni = a "+str(pieno))
    print(str(pieniTotali),str(vuotiTotali))

checkFile()
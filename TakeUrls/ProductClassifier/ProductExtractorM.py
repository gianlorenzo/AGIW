import os
import pandas as pd
from pandas import DataFrame
import numpy as np
import logging
from datetime import datetime
import sys


#dir che porta alla cartella occurrence extractor
dirInputNotebook = "/home/gianlorenzo/AGIW/notebook/"
dirGlobaleDav = "/home/gianlorenzo/AGIW/occurrence-extractor"
dirOutputGlobaleDav="/home/gianlorenzo/AGIW/Step1/"
comandoDir="cd "+dirGlobaleDav
comandoClassifier="python2.7 -m src.model.specificationextractor "
# se nella cartella ci sta solo un index non la analizzo
#checkDir mi dice quanti oggetti ci sono in una cartella
def checkDir(dir):
    # print(len([name for name in os.listdir(dir) if os.path.isfile(os.path.join(dir, name))]))
    return (len(os.listdir(dir)))

#gli passo la dir di notebook
#scansiono le cartelle
#se nella cartella ci sta solo il file index passo alla prossima (checkdir==1)
#altrimenti eseguo il metodo per ciascun link del file index,gia ripulito dai link tarocchi
def getProductSpecifies(dirInputNotebook):
    os.mkdir(dirOutputGlobaleDav)
    log = open("/home/gianlorenzo/AGIW/Step1/writeLogJson.log","a")
    sys.stdout = log
    print("start "+datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    logging.warning("start "+datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    os.system(comandoDir)
    listadir = os.listdir(dirInputNotebook)
    for dir in listadir:
	print("sono nella cartella: "+str(dir))
	logging.warning("sono nella cartella: "+str(dir))
        if not checkDir(dirInputNotebook+dir)==1:
            os.mkdir(dirOutputGlobaleDav+dir)
            URLBuone = getReachable_Links(dir)
	    a = 1
            for i in URLBuone:
                #applico il classificatore
                os.system(comandoClassifier+" "+i+" "+dirOutputGlobaleDav+dir+"/"+str(a))
		print("Nella cartella: "+str(dir)+" ho scritto il file: " + str(a)+".json")
		logging.warning("Nella cartella: "+str(dir)+" ho scritto il file: " + str(a)+".json")
		a = a+1
    logging.warning("fine " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print("fine " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))





#prendo il file index e lo trasformo in una matrice :link,errore/nomefile
#seleziono solo le righe corrette
#seleziono solo la colonna dei links
#inserisco tutti i link in un array
def getReachable_Links(dir):
    with open("/home/gianlorenzo/AGIW/notebook/"+dir+"/index.txt") as f:

        linksMatrix = pd.read_table(f,header=None, names=['Link', 'Esito'])
    print(type(linksMatrix))
    htmls=[]
    #mi creo un array con dentro i .html
    for i in np.asarray(linksMatrix["Esito"]):
        if str(i).endswith(".html"):
            htmls.append(i)

    #link matrix formattata con solo righe di html
    linksMatrixFormatted=linksMatrix.loc[linksMatrix["Esito"].isin(htmls)]
    #restituisco lista di html puliti
    return np.asarray(linksMatrixFormatted["Link"])

getProductSpecifies(dirInputNotebook)


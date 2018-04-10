import os
import pandas as pd
from pandas import DataFrame
import numpy as np

#dir che porta alla cartella occurrence extractor
dirInputNotebook = "/home/gianlorenzo/AGIW/notebook"
dirGlobaleDav = "/home/gianlorenzo/AGIW/app/occurrence-extractor"
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
def getProductSpecifies(dirNotebook):
    os.mkdir(dirOutputGlobaleDav)
    os.system(comandoDir)
    listadir = os.listdir(dirNotebook)
    for dir in listadir:
        if not checkDir(dirNotebook+dir)==1:
            os.mkdir(dirOutputGlobaleDav+dir)
            URLBuone = getReachable_Links(dir)
            for i in URLBuone:
                #applico il classificatore
                os.system(comandoClassifier+" "+i+" "+dirOutputGlobaleDav+dir+i.json)


#prendo il file index e lo trasformo in una matrice :link,errore/nomefile
#seleziono solo le righe corrette
#seleziono solo la colonna dei links
#inserisco tutti i link in un array
def getReachable_Links(dir):
    with open(dir+"/index.txt") as f:

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

dirConUrl_Error = "/home/davben/AGIW/notebook/www.shopwithjoe.com"
dirConURl = "/home/davben/AGIW/notebook/www.shopandship.co.za"
dirSenzaUrl="/home/davben/AGIW/notebook/53laptop.com"

#print(getReachable_Links("/home/davben/AGIW/notebook/www.shopwithjoe.com"))
print(checkDir(dirSenzaUrl))
#df.loc[df[["B"].endswith(".html")]

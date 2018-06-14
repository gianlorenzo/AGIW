from ProductClassifier import GetKeywords as gk

import logging
from googletrans import Translator


AGIWdir = "/home/gianlorenzo/AGIW/"

def getTable(dir,soup):
    #log = open("tableLog.log","a")
    #sys.stdout = log
    kwFile = open(AGIWdir+"keywordsPrimarie.txt", "r")
    table = soup.find_all("table")
    array = []
    listKWSecondarie = gk.keywords(dir,soup)
    translator = Translator()
    listKWPrimarie = gk.getListKWPrimarie(kwFile)
    try:
        language = soup.find_all("html")[0]["lang"].split("-")[0].text
        listKWPrimarieTradotto = []
        for k in listKWPrimarie:
            listKWPrimarieTradotto.append(translator.translate(k.strip(), dest=language))
        listKWPrimarie = listKWPrimarieTradotto
    except:
        print("Html Language: english")
    logging.warning("lista keyWords Secondarie : ")
    logging.warning(listKWSecondarie)
    if len(table)==0:
        return array
    for t in table:
        string = str(t)
        for keyW in listKWPrimarie:
            if keyW in string:
                    if not t in array:
                        # print(str(t))
                        array.append(t)
    if len(array)==0:
        logging.warning("la lunghezza di table con kprimarie = 0")
        array = []
        #if(len(table)==0):
        #    return array
        bestTag = gk.bestArea(table, listKWSecondarie)
        logging.warning("best tag in table con ksec = 0 "+ str(bestTag))
        if (bestTag == None):
            return array
        array.append(bestTag)
    if len(array)>1:
        logging.warning("la lunghezza di table con kprimarie >1")
        bestTag = gk.bestArea(array,listKWSecondarie)
        array=[]
        if (bestTag == None):
            return array
        array.append(bestTag)

    return array


def getUl(dir, soup):
    # log = open("tableLog.log","a")
    # sys.stdout = log
    kwFile = open(AGIWdir + "keywordsPrimarie.txt", "r")
    ul = soup.find_all("ul")
    array = []
    listKWSecondarie = gk.keywords(dir, soup)
    translator = Translator()
    listKWPrimarie = gk.getListKWPrimarie(kwFile)
    try:
        language = soup.find_all("html")[0]["lang"].split("-")[0].text
        listKWPrimarieTradotto = []
        for k in listKWPrimarie:
            listKWPrimarieTradotto.append(translator.translate(k.strip(), dest=language))
        listKWPrimarie = listKWPrimarieTradotto
    except:
        print("Html Language: english")

    for u in ul:
        string = str(u)
        for keyW in listKWPrimarie:
            if keyW in string:
                if not u in array:
                    # print(str(t))
                    array.append(u)
    if len(array) == 0:
    #non ci sono parole chiavi primarie
        logging.warning("lunghezza array UL con kPRimarie: 0")
        logging.warning("numero ul della pagina: "+str(len(ul)))
        array = []
        if len(ul)==0:
            return array
        bestTag = gk.bestArea(ul, listKWSecondarie)
        if (bestTag == None):
            return array
        array.append(bestTag)
    if len(array) > 1:
        logging.warning("lunghezza array ul: "+str(len(array)))
        #in samsclub il file 11 html era schifoso aveva ul con parola product ma nessuna keyword rilevante
        #j = 0
        #for i in array:
        #    file = open(AGIWdir+"provaD/"+str(j)+".txt","w+")
        #    file.write(str(i))
        #    j=j+1

        bestTag = gk.bestArea(array, listKWSecondarie)
        array = []
        if (bestTag == None):
            return array
        array.append(bestTag)

    return array


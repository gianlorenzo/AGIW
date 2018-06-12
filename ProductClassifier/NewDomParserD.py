import os
from datetime import datetime
import logging
import codecs
import bs4
import sys
from googletrans import Translator
import json


AGIWdir = "/home/davben/AGIW/"
ProvaTdir = "provaT/"

def checkDir(dir):
    # print(len([name for name in os.listdir(dir) if os.path.isfile(os.path.join(dir, name))]))
    return (len(os.listdir(dir)))

def checkAreaWords(stringX,wordList):
    score = 0
    #logging.warning(stringX)
    for word in wordList:
        #logging.warning("21")
        #logging.warning(word)
        if word in stringX or word.lower() in stringX:
            score = score +1

    return score

def bestArea(listaTableOrUl,wordList):
    bestTag = listaTableOrUl[0]
    for (tag) in listaTableOrUl[1:]:
        string = str(tag)
        if checkAreaWords(str(bestTag),wordList)<checkAreaWords(string,wordList):
            bestTag = tag

    logging.warning("il best tag ha KEYWORDS SECONDARIE  : "+str(checkAreaWords(str(bestTag),wordList)))
    #se non ci sono piu di 2 keywords allora ipotizzo che quel tag sia un fake e non riturno nulla
    if checkAreaWords(str(bestTag),wordList)<4:
        return None
    return bestTag


def keywords(nomeDominio,soup):
    #log = open("kwLog.log","a")
    #sys.stdout = log
    #if(not soup.title == None):
    title = soup.title.string.replace(",","").split(" ")
    #title ="$"

    #logging.warning(str(title))
    #logging.warning("titolo principale: ok")
    try:

        #logging.warning("secondo titolo: ok")
        keywords = soup.select('meta[name="keywords"]')[0]['content'].lower().split(",")

        #logging.warning("keywords: ok")
        if nomeDominio in keywords:
            keywords.remove(nomeDominio)

        cleaned_keywords = []

        for t in title:
            cleaned_keywords.append(t)

        for k in keywords:
            cleaned_keywords.append(k)

        #logging.warning("ritorna cleaned_keywords")

        return cleaned_keywords
    except:
       #logging.warning("ritorna title fuori")
       return ((title))


#modificarlo e fare in modo che viene scelto il title se le keywords sono poche
def keywordsUl(nomeDominio,soup):
    #log = open("kwLog.log","a")
    #sys.stdout = log

    #logging.warning(str(title))
    #logging.warning("titolo principale: ok")
    try:
        #logging.warning("secondo titolo: ok")
        keywords = soup.select('meta[name="keywords"]')[0]['content'].lower().split(",")

        #logging.warning("keywords: ok")
        if nomeDominio in keywords:
            keywords.remove(nomeDominio)

        cleaned_keywords = []

        for k in keywords:
            cleaned_keywords.append(k)

        #logging.warning("ritorna cleaned_keywords")

        return cleaned_keywords
    except:
       #logging.warning("ritorna title fuori")
       return []

def getListKWPrimarie(kwFile):
    l=[]
    for line in kwFile.readlines():
        l = l + (line.split())
    return l

def getTable(dir,soup):
    #log = open("tableLog.log","a")
    #sys.stdout = log
    kwFile = open(AGIWdir+"keywordsPrimarie.txt", "r")
    table = soup.find_all("table")
    array = []
    listKWSecondarie = keywords(dir,soup)
    translator = Translator()
    listKWPrimarie = getListKWPrimarie(kwFile)
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
        bestTag = bestArea(table, listKWSecondarie)
        logging.warning("best tag in table con ksec = 0 "+ str(bestTag))
        if (bestTag == None):
            return array
        array.append(bestTag)
    if len(array)>1:
        logging.warning("la lunghezza di table con kprimarie >1")
        bestTag = bestArea(array,listKWSecondarie)
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
    listKWSecondarie = keywords(dir, soup)
    translator = Translator()
    listKWPrimarie = getListKWPrimarie(kwFile)
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
        bestTag = bestArea(ul, listKWSecondarie)
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

        bestTag = bestArea(array, listKWSecondarie)
        array = []
        if (bestTag == None):
            return array
        array.append(bestTag)

    return array



def getTagsFeatures():
    log = open("logFile.log","a")
    sys.stdout = log
    os.mkdir(AGIWdir+"FINALJSON")
    log = open(AGIWdir+"FINALJSON/writeLogJson.log", "a")
    sys.stdout = log
    print("start " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    logging.warning("start " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    listaDir = os.listdir(AGIWdir+ProvaTdir)
    for dir in listaDir:
        print("sono nella cartella: " + str(dir))
        logging.warning("sono nella cartella: " + str(dir))
        if not checkDir(AGIWdir+ProvaTdir + dir) == 1:
            os.mkdir(AGIWdir+"FINALJSON/" + dir)
            listaFile = os.listdir(AGIWdir+ProvaTdir + dir)
            listaFile.remove("index.txt")
            listaFile.sort()

            for file in listaFile:
                os.mkdir(AGIWdir+"FINALJSON/" + dir + "/" + file)
                f = codecs.open(AGIWdir+ProvaTdir + dir + "/" + file, 'r')
                html = f.read()
                soup = bs4.BeautifulSoup(html, "html.parser")
                #se il titolo non cè è una pagina robot!
                if(soup.title and soup.title.string):
                    logging.warning("file: " + str(file))

                    table = getTable(dir,soup)
                    #logging.warning((table))
                    logging.warning("lunghezza table Depurata :" + str(len(table)))

                    ul = getUl(dir,soup)
                    logging.warning("lunghezza Ul Depurata :"+str(len(ul)))
                    oT = []
                    oU = []
                    if not (len(table)==0) :
                        for t in table:
                            logging.warning("table: ok ")
                            for row in t.find_all('tr'):
                                if "th" in str(row):
                                    for th in row.find_all('th'):
                                        if "function" in th.text or "<!--" in th.text:
                                            th.decompose()
                                        else:
                                            text = th.text.encode('ascii', errors='ignore')
                                            oT.append(str(text).strip().replace("\\n", "").replace("b'", "").replace("\\t","").replace("\"",""))
                                    for td in row.find_all('td'):
                                        if "function" in td.text or "<!--" in td.text:
                                            td.decompose()
                                        else:
                                            text = td.text.encode('ascii', errors='ignore')
                                            oT.append(str(text).strip().replace("\\n", "").replace("b'", "").replace("\\t","").replace("\"",""))
                                        logging.warning("ot finale con th"+ str(oT))

                                else:
                                    for td in row.find_all('td'):
                                            if "function" in td.text or "<!--" in td.text:
                                                td.decompose()
                                            else:
                                                text = td.text.encode('ascii', errors='ignore')
                                                oT.append(str(text).strip().replace("\\n","").replace("b'","").replace("\\t","").replace("\"",""))
                                logging.warning("ot finale senza th"+ str(oT))
                        i = 0
                        dictT = {}
                        while (i < len(oT) - 1):
                            dictT[oT[i]] = oT[i + 1]
                            i = i + 2

                        fileT = open(AGIWdir+"FINALJSON/" + dir + "/" + file + "/table.json", "w+")
                        json.dump(dictT, fileT)
                        fileT.close()
                    #se non ci sono tabelle con keywords cerco nelle liste
                    else:
                        for u in ul:
                            for li in u.find_all("li"):
                                text = li.text.encode('ascii',errors='ignore')
                                oU.append(str(text).replace("\\n","").replace("b'","").replace("\\t","").replace("\"",""))
                        logging.warning("li finale" + str(oU))


                        dictU = {}
                        dictU["Features:"] = oU

                        fileU = open(AGIWdir+"FINALJSON/" + dir + "/" + file + "/ul.json", "w+")

                        json.dump(dictU, fileU)
                        fileU.close()



        logging.warning("fine " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        print("fine " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


getTagsFeatures()
import os
import codecs
import bs4
import logging
import sys
from googletrans import Translator
from datetime import datetime
import json
import string

def keywords(name,soup,found_titles):
    #log = open("kwLog.log","a")
    #sys.stdout = log
    title = soup.title.string.split(" ")
    #logging.warning(str(title))
    #logging.warning("titolo principale: ok")
    try:
        title = soup.title.string.lower()
        #logging.warning("secondo titolo: ok")
        keywords = soup.select('meta[name="keywords"]')[0]['content'].lower().split(",")
        #logging.warning("keywords: ok")
        if name in keywords:
            keywords.remove(name)

        cleaned_keywords = []

        for k in keywords:
            for k in title:
                cleaned_keywords.append(k)

        #logging.warning("ritorna cleaned_keywords")
        return cleaned_keywords

    except:
       #logging.warning("ritorna title fuori")
       return title



def getTable(dir,soup):
    #log = open("tableLog.log","a")
    #sys.stdout = log
    kwFile = open("/home/gianlorenzo/AGIW/keywordsPrimarie.txt", "r")
    table = soup.find_all("table")
    array = []
    kw = keywords(dir,soup,[])
    translator = Translator()
    for t in table:
        string = str(t)
        if kw:
           for key in kw:
               #print("kw:"+str(key))
               if key in string:

                   if not t in array:
                      # print(str(t))
                       array.append(t)
        else:
            try:
                for line in kwFile.readlines():
                    newLine = translator.translate(line.strip(), dest=soup.find_all("html")[0]['lang'].split("-")[0]).text
                    #print("line"+str(newLine))
                    if newLine in string:

                        if not t in array:
                            #print(str(t))
                            array.append(t)

            except:
                print("Html Language: english")
    return array

def getUl(dir,soup):
    #log = open("ulLog.log", "a")
    #sys.stdout = log
    kwFile = open("/home/gianlorenzo/AGIW/keywordsPrimarie.txt", "r")
    ul = soup.find_all("ul")
    array = []
    kw = keywords(dir, soup, [])
    translator = Translator()
    for u in ul:
        print(str(u))
        string = str(ul)
        if kw:
            for key in kw:
                if key in string:

                    if not u in array:
                        array.append(u)
                        print(str(array))
                       # logging.warning("non tradotto u e scrivo array")

                       # logging.warning(str(array))
        else:
            try:
                for line in kwFile.readlines():
                    newLine = translator.translate(line.strip(), dest=soup.find_all("html")[0]['lang'].split("-")[0]).text
                    #print("line"+str(newLine))
                    if newLine in string:

                        if not u in array:
                            #logging.warning("tradotto u e scrivo array")
                            array.append(u)
                           # logging.warning(str(array))

            except:
                print("English Language")
    #logging.warning("ritorna array")
    #logging.warning("array finale" + str(array))

    return array


def checkDir(dir):
    # print(len([name for name in os.listdir(dir) if os.path.isfile(os.path.join(dir, name))]))
    return (len(os.listdir(dir)))


def getTagsFeatures():
    log = open("logFile.log","a")
    sys.stdout = log
    os.mkdir("/home/gianlorenzo/AGIW/FINALJSON")
    log = open("/home/gianlorenzo/AGIW/FINALJSON/writeLogJson.log", "a")
    sys.stdout = log
    print("start " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    logging.warning("start " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    listaDir = os.listdir("/home/gianlorenzo/AGIW/provaT/")
    for dir in listaDir:
        print("sono nella cartella: " + str(dir))
        logging.warning("sono nella cartella: " + str(dir))
        if not checkDir("/home/gianlorenzo/AGIW/provaT/" + dir) == 1:
            os.mkdir("/home/gianlorenzo/AGIW/FINALJSON/" + dir)
            listaFile = os.listdir("/home/gianlorenzo/AGIW/provaT/" + dir)
            listaFile.remove("index.txt")
            listaFile.sort()
            j = 1
            for file in listaFile[0:3]:
                os.mkdir("/home/gianlorenzo/AGIW/FINALJSON/" + dir + "/" + str(j) + ".html")
                f = codecs.open("/home/gianlorenzo/AGIW/provaT/" + dir + "/" + file, 'r')
                html = f.read()
                soup = bs4.BeautifulSoup(html, "html.parser")
                logging.warning("file: " + str(file))

                table = getTable(dir,soup)
                logging.warning("presa table: ok ")

                ul = getUl(dir,soup)
                logging.warning("presa ul: ok ")
                oT = []
                oU = []
                #if table:
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
                for u in ul:
                    for li in u.find_all("li"):
                        text = li.text.encode('ascii',errors='ignore')
                        oU.append(str(text).replace("\\n","").replace("b'","").replace("\\t","").replace("\"",""))
                logging.warning("li finale" + str(oU))

                i = 0
                dictT = {}
                while (i < len(oT) - 1):
                    dictT[oT[i]] = oT[i + 1]
                    i = i + 2


                dictU = {}
                dictU["Features:"] = oU

            fileT = open("/home/gianlorenzo/AGIW/FINALJSON/" + dir + "/" + str(j) + ".html" + "/" + str(j) + "-table.json", "w+")
            json.dump(dictT, fileT)
            fileT.close()


            fileU = open("/home/gianlorenzo/AGIW/FINALJSON/" + dir + "/" + str(j) + ".html" + "/" + str(j) + "-ul.json", "w+")

            json.dump(dictU, fileU)
            fileU.close()



            print("sono nella cartella: " + str(dir) + " ho scritto il file" + str(j) + "-table.json")
            logging.warning("sono nella cartella: " + str(dir) + " ho scritto il file" + str(j) + ".json")
            j = j + 1


        logging.warning("fine " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        print("fine " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))





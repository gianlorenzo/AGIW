import os
from datetime import datetime
import logging
import codecs
import bs4
import sys
import json
from ProductClassifier import GetKeywords as gk
from ProductClassifier import GetTableAndUl as gt

AGIWdir = "/home/gianlorenzo/AGIW/"
dirHtml = "notebook/"
dirOutput = "Json"

def getTagsFeatures():
    log = open("logFile.log","a")
    sys.stdout = log
    os.mkdir(AGIWdir+dirOutput)
    log = open(AGIWdir+dirOutput+"/"+"writeLogJson.log", "a")
    sys.stdout = log
    print("start " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    logging.warning("start " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    listaDir = os.listdir(AGIWdir + dirHtml)
    for dir in listaDir:
        print("sono nella cartella: " + str(dir))
        logging.warning("sono nella cartella: " + str(dir))
        if not gk.checkDir(AGIWdir + dirHtml + dir) == 1:
            os.mkdir(AGIWdir+dirOutput+"/" + dir)
            listaFile = os.listdir(AGIWdir + dirHtml + dir)
            listaFile.remove("index.txt")
            listaFile.sort()

            for file in listaFile:
                os.mkdir(AGIWdir+dirOutput+"/" + dir + "/" + file)
                f = codecs.open(AGIWdir + dirHtml + dir + "/" + file, 'r')
                html = f.read()
                soup = bs4.BeautifulSoup(html, "html.parser")
                #se il titolo non cè è una pagina robot!
                if(soup.title and soup.title.string):
                    logging.warning("file: " + str(file))

                    table = gt.getTable(dir,soup)
                    logging.warning("lunghezza table Depurata :" + str(len(table)))

                    ul = gt.getUl(dir,soup)
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
                                            if "function" in td.text or "<!--" in td.text or "var" in td.text or "http" in td.text:
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

                        fileT = open(AGIWdir+dirOutput+"/" + dir + "/" + file + "/table.json", "w+")
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

                        fileU = open(AGIWdir+dirOutput+"/" + dir + "/" + file + "/ul.json", "w+")

                        json.dump(dictU, fileU)
                        fileU.close()



        logging.warning("fine " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        print("fine " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))



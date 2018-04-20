import os
import codecs
import bs4
import logging
import sys
from googletrans import Translator


def keywords(name,soup,found_titles):
    log = open("kwLog.log","a")
    sys.stdout = log
    title = soup.title.string.split(" ")
    try:
        title = soup.title.string.lower()
        keywords = soup.select('meta[name="keywords"]')[0]['content'].lower().split(",")

        if name in keywords:
            keywords.remove(name)

        cleaned_keywords = []

        for k in keywords:
            for k in title:
                cleaned_keywords.append(k)

        return cleaned_keywords
    except:
       return title

def getTable(dir,soup):
    log = open("tableLog.log","a")
    sys.stdout = log
    kwFile = open("/home/gianlorenzo/AGIW/keywordsPrimarie.txt", "r")
    table = soup.find_all("table")
    array = []
    kw = keywords(dir,soup,[])
    translator = Translator()
    for t in table:
        string = str(t)
        if kw:
           for key in kw:
               print("kw:"+str(key))
               if key in string:
                   print("kw"+str(key))
                   print("table"+str(t))
                   if not t in array:
                       array.append(t)
        else:
            try:
                for line in kwFile.readlines():
                    newLine = translator.translate(line.strip(), dest=soup.find_all("html")[0]['lang'].split("-")[0]).text
                    print("line"+str(newLine))
                    if newLine in string:
                        print("line"+str(newLine))
                        print("stringa"+str(string))
                        if not t in array:
                            print("table"+str(t))
                            array.append(t)

            except:
                print("Html Language: english")
    return array

def getTagsFeatures():
    log = open("logFile.log","a")
    sys.stdout = log
    trainDom = os.listdir("/home/gianlorenzo/Scrivania/FolderTrain/")
    for dir in trainDom:
        logging.warning("Sono nel cartella:" +  str(dir))
        print("Sono nel cartella:" +  str(dir))
        listaDir = os.listdir("/home/gianlorenzo/Scrivania/FolderTrain/"+dir)
        for dirHtml in listaDir:
            logging.warning("Sono nel cartella:" + str(dirHtml))
            print("Sono nel cartella:" + str(dirHtml))

            file = codecs.open("/home/gianlorenzo/AGIW/notebook/"+dir+"/"+dirHtml,"r")
            soup = bs4.BeautifulSoup(file.read(), "html.parser")
            titleFile = open("/home/gianlorenzo/Scrivania/FolderTrain/"+dir+"/"+dirHtml+"/title.txt","w+")
            tableFile = open("/home/gianlorenzo/Scrivania/FolderTrain/"+dir+"/"+dirHtml+"/table.txt","w+")

            ulFile = open("/home/gianlorenzo/Scrivania/FolderTrain/" + dir + "/" + dirHtml + "/ul.txt", "w+")
            metaKWFile = open("/home/gianlorenzo/Scrivania/FolderTrain/" + dir + "/" + dirHtml + "/metaKW.txt", "w+")
            #structFile = open("/home/gianlorenzo/Scrivania/FolderTrain/" + dir + "/" + dirHtml + "/struct.txt", "w+")

            for t in soup.find_all("title"):
                titleFile.write(str(t))

            table = getTable(dir,soup)

            for tb in table:
                tableFile.write(str(tb))

            for u in soup.find_all("ul"):
                ulFile.write(str(u))
            try:
                metaKw = soup.select('meta[name="keywords"]')[0]['content'].lower()
                if metaKw:
                    for kw in metaKw:
                        metaKWFile.write(kw)
            except:
                metaKWFile.write(soup.find("title").text)

            titleFile.close()

            tableFile.close()

            ulFile.close()

            metaKWFile.close()

getTagsFeatures()
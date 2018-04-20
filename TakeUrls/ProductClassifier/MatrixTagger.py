import os
import codecs
import bs4
import logging
import sys


def keywords(name,found_titles,soup):
    try:
        title = soup.title.string.lower()
        keywords = soup.select('meta[name="keywords"]')[0]['content'].lower().split(",")


        if name in keywords:
            keywords.remove(name)

        cleaned_keywords    = []

        for k in keywords:
            for k in title:
                cleaned_keywords.append(k)
        if(len(cleaned_keywords))>0 and title not in found_titles:
            found_titles.append(title)

        return cleaned_keywords
    except:
        print("no keywords")

def getTable(dir,soup):
    table = soup.find_all("table")
    array = []
    kw = keywords(dir,[],soup)
    for t in table:
        string = str(t)
        if kw:
           for key in kw:
                if key in string:
                    array.append(t)
        else:
            if "Product:" in string or "product:" in string or "price" in string or "Price" in string:
                array.append(t)
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

            metaKw = keywords(dir,[],soup)
            if metaKw:
                for kw in metaKw:
                    metaKWFile.write(str(kw))

            titleFile.close()

            tableFile.close()

            ulFile.close()

            metaKWFile.close()


getTagsFeatures()









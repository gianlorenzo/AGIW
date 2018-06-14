import os
import logging

AGIWdir = "/home/gianlorenzo/AGIW/"


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

def getListKWPrimarie(kwFile):
    l=[]
    for line in kwFile.readlines():
        l = l + (line.split())
    return l


def keywords(nomeDominio,soup):
    title = soup.title.string.replace(",","").split(" ")
    try:
        keywords = soup.select('meta[name="keywords"]')[0]['content'].lower().split(",")
        if nomeDominio in keywords:
            keywords.remove(nomeDominio)

        cleaned_keywords = []

        for t in title:
            cleaned_keywords.append(t)

        for k in keywords:
            cleaned_keywords.append(k)
        return cleaned_keywords
    except:
        return (title)


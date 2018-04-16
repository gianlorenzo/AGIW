import codecs
import logging
import bs4
import json
import os
import sys
from datetime import datetime


def checkDir(dir):
    # print(len([name for name in os.listdir(dir) if os.path.isfile(os.path.join(dir, name))]))
    return (len(os.listdir(dir)))

def takeTable():
    os.mkdir("/home/gianlorenzo/AGIW/JSONSTEP1(4)")
    log = open("/home/gianlorenzo/AGIW/JSONSTEP1(4)/writeLogJson.log","a")
    sys.stdout = log
    print("start " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    logging.warning("start " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    listaDir = os.listdir("/home/gianlorenzo/AGIW/OurStep1/")
    for dir in listaDir:
        print("sono nella cartella: " + str(dir))
        logging.warning("sono nella cartella: " + str(dir))
        if not checkDir("/home/gianlorenzo/AGIW/OurStep1/"+dir)==1:
            os.mkdir("/home/gianlorenzo/AGIW/JSONSTEP1(4)/"+dir)
            listaFile = os.listdir("/home/gianlorenzo/AGIW/OurStep1/"+dir)
            listaFile.remove("index.txt")
            listaFile.sort()
            j=1
            for file in listaFile:
                f = codecs.open("/home/gianlorenzo/AGIW/OurStep1/"+dir+"/"+file, 'r')
                html = f.read()

                soup = bs4.BeautifulSoup(html, "html.parser")

                table = soup.find_all("table")
                array = []
                kw = keywords(dir,file,dir,[])
                for t in table:
                    string = str(t)
                    if kw:
                        for key in kw:
                            if key in string:
                                array.append(t)
                    else:
                        if "Product:" in string or "product:" in string or "price" in string or "Price" in string:
                            array.append(t)
                o = []
                for t in array:
                    for row in t.find_all('tr'):
                        if "th" in str(row):
                            for th in row.find_all('th'):
                                if "function" in th.text or "<!--" in th.text:
                                    th.decompose()
                                else:
                                    o.append(th.text.strip())
                            for td in row.find_all('td'):
                                if "function" in td.text or "<!--" in td.text:
                                    td.decompose()
                                else:
                                    o.append(td.text.strip())
                        else:
                            for td in row.find_all('td'):
                                if "function" in td.text or"<!--" in td.text:
                                    td.decompose()
                                else:
                                    o.append(td.text.strip())
                i = 0
                dict = {}
                while (i < len(o) - 1):
                    dict[o[i]] = o[i + 1]
                    i = i + 2
                file = open("/home/gianlorenzo/AGIW/JSONSTEP1(4)/"+dir+"/"+str(j)+".json", "w+")
                json.dump(dict, file)
                file.close()
                print("sono nella cartella: " + str(dir)+" ho scritto il file"+str(j)+".json")
                logging.warning("sono nella cartella: " + str(dir)+" ho scritto il file"+str(j)+".json")
                j = j + 1
    logging.warning("fine " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print("fine " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))



def keywords(dir,file,name,found_titles):
    f = codecs.open("/home/gianlorenzo/AGIW/OurStep1/" + dir + "/" + file, 'r')
    html = f.read()
    soup = bs4.BeautifulSoup(html, "html.parser")

    try:
        title = soup.title.string.lower()
        keywords = soup.select('meta[name="keywords"]')[0]['content'].lower().split(",")


        if name in keywords:
            keywords.remove(name)

        cleaned_keywords = []

        for k in keywords:
            for k in title:
                cleaned_keywords.append(k)
        if(len(cleaned_keywords))>0 and title not in found_titles:
            found_titles.append(title)

        return cleaned_keywords
    except:
        print("no keywords")

takeTable()
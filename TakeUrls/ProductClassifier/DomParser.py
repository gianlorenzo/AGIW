import parsel
import codecs
import pandas as pd
import re
import bs4
import json
import lxml.html
import os

def takeTable():
    listaFile = os.listdir("/home/gianlorenzo/AGIW/notebook/www.zumthing.com")
    j = 0
    listaFile.remove("index.txt")
    listaFile.sort()
    for file in listaFile:
        print(file)
        f = codecs.open("/home/gianlorenzo/AGIW/notebook/www.zumthing.com/"+file, 'r')
        html = (f.read())
        soup = bs4.BeautifulSoup(html, "lxml")
        table = soup.find_all("table")
        array = []
        for t in table:
            string = str(t)
            if "Product:" in string or "product:" in string or "price" in string or "Price" in string:
                array.append(t)
        o = []
        for t in array:
            for row in t.find_all('tr'):
                if "th" in str(row):
                    for th in row.find_all('th'):
                        o.append(th.text.strip())
                    for td in row.find_all('td'):
                        o.append(td.text.strip())
                else:
                    for td in row.find_all('td'):
                        o.append(td.text.strip())
        i = 0
        dict = {}
        while (i < len(o) - 1):
            dict[o[i]] = o[i + 1]
            i = i + 2
        file = open(str(j)+".json", "w+")
        json.dump(dict, file)
        file.close()
        j= j+1

takeTable()








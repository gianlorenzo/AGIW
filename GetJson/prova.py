import codecs
import logging
import bs4
import json
import os
import sys
from datetime import datetime
dir = "www.superbiiz.com"
file = "4.html"
os.mkdir("/home/davben/AGIW/JSONSTEP1")
os.mkdir("/home/davben/AGIW/JSONSTEP1/"+dir)
f = codecs.open("/home/davben/AGIW/notebook/"+dir+"/"+file, 'r')
html = (f.read())
soup = bs4.BeautifulSoup(html, "html.parser")
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
                                        if not "function" in th.text or not "<!--" in th.text:
                                            o.append(th.text.strip())
                                    for td in row.find_all('td'):
                                        if not "function" in td.text or not "<!--" in td.text:
                                            o.append(td.text.strip())
                                else:
                                    for td in row.find_all('td'):
                                        if not "function" in td.text or not "<!--" in td.text:
                                            o.append(td.text.strip())
                        i = 0
                        dict = {}
                        while (i < len(o) - 1):
                            dict[o[i]] = o[i + 1]
                            i = i + 2
                        file = open("/home/davben/AGIW/JSONSTEP1/"+dir+"/"+str(1)+".json", "w+")
                        json.dump(dict, file)
                        file.close()
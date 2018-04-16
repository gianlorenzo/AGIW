import codecs
import logging
import bs4
import json
import parsel
import re

dir = "www.superbiiz.com"
file = "4.html"
f = codecs.open("/home/gianlorenzo/AGIW/notebook/"+dir+"/"+file, 'r')


dir1 = "/home/davben/AGIW/FileProvaClassifier/28/28.html"
dir2 = "/home/davben/AGIW/FileProvaClassifier/39/39.html"
dir3 = "/home/davben/AGIW/FileProvaClassifier/4/4.html"
dir4 = "/home/davben/AGIW/FileProvaClassifier/1/1.html"


f=codecs.open("/home/gianlorenzo/AGIW/notebook/"+dir+"/"+file, 'r')
html = (f.read())
array=[]
arrayx = []
a = []
b = []
soup = bs4.BeautifulSoup(html, "html.parser")
table = soup.find_all("ul")
for element in table:
    element.extract()

for t in table:
    string = str(t)
    #string.replace("<!--(.*?)-->"," ")
    if "Product:" in string or "product:" in string or "price" in string or "Price" in string:
        array.append(str(t))
#if(len(array)==0):
#print(table[1])
doc = parsel.Selector(text=html)
element = doc.xpath("//ul")
parent = element.xpath("//li//text()")
print(parent)
for i in element:
    for descendant in i.xpath("descendant::*"):
        for txt in descendant.xpath("//text()"):
            if ("Product:" in txt or "product:" in txt or "price" in string or "Price" in txt):
                arrayx.append()






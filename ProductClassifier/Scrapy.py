import codecs
import parsel
import re


def prova():
    dir = "/home/gianlorenzo/AGIW/FileProvaClassifier/28.html"
    dir2 = "/home/gianlorenzo/AGIW/FileProvaClassifier/39.html"
    f=codecs.open(dir2, 'r')
    html = (f.read())
    a = []
    b = []
    dict = {}
    doc = parsel.Selector(text=html)
    element = doc.xpath('//table')
    for i in element.xpath("//tr/td/text()"):
        a.append(re.search("data='(.+?)'",str(i)).group(1).strip())
        #for i in element.xpath("//tr/td/[(normalize-space(text()))]"):
        for j in element.xpath("//tr/td/*/text()"):

            dict[re.search("data='(.+?)'",str(j)).group(1).strip()] = re.search("data='(.+?)'",str(i)).group(1).strip()
    return dict


print(prova())
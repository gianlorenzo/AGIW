import codecs
import logging
import bs4
import json
import parsel
import re

dir = "www.superbiiz.com"
file = "4.html"
f = codecs.open("/home/davben/AGIW/notebook/"+dir+"/"+file, 'r')


dir = "/home/davben/AGIW/FileProvaClassifier/28/28.html"
dir2 = "/home/davben/AGIW/FileProvaClassifier/39/39.html"
dir3 = "/home/davben/AGIW/FileProvaClassifier/4/4.html"
dir4 = "/home/davben/AGIW/FileProvaClassifier/1/1.html"


f=codecs.open(dir4, 'r')
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
print(element.xpath("//text()"))
parent = element.xpath("..")
print((element))
print(parent)
for i in element:
    for descendant in i.xpath("descendant::*"):
        for txt in descendant.xpath("//text()")
            if ("Product:" in txt or "product:" in txt or "price" in string or "Price" in txt):
                arrayx.append()





#print(len(array))
#print(array[0])
if(len(array)>1):
    for i in array:
        if("itemprop" in str(i) or "Specifications" in str(i)):
            arrayx.append(i)

if(len(arrayx)>0):
    arrays = arrayx
else:
    arrays=array

doc = parsel.Selector(text=html)
element = doc.xpath('//ul')
    #print((element))
    #print(str(i))
for i in element.xpath("//*/*/text()"):
    if(not str(i).endswith('\\n\'>')):
        if(not re.search("data='(.+?)'",str(i)) == None):
            a.append((re.search("data='(.+?)'",str(i)).group(1)))

#for i in a:
#    print(i)

    #a.append((re.search("data='(.+?)'",str(i).replace("\\n","")).group(1)))
    #for i in element.xpath("//tr/td/[(normalize-space(text()))]"):
    #for i in element.xpath("//tr/td/text()"):
    #b.append(str(i))
    #b.append(re.search("data='(.+?)'",str(i)).group(1).replace("\\n",""))
    #print(len(b))
    #df = pd.DataFrame({"a":a,"b":b[:60]})
    #df.loc[not pd.DataFrame["b"]=='\n']
    #print ((df[0:8]))
    #for elem2 in b:
    # json.write(elem2+"\n")
    #json.close()
    #df = pd.DataFrame({"a":a,"b":b[:170]})
    #print(df[100:])
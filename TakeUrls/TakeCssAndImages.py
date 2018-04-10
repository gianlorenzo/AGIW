
from urllib.request import (urlretrieve,urlparse,urlunparse)


import TakeUrls
import os
def takeImage(url):

    soup = TakeUrls.takeHtmlContent(url)
    i = 0
    for image in soup.find_all("img"):
        img = image['src']
        y = str(img)
        path = y.split("/",-1)[-1]
        print (path)
        i = i+1

def takeImage2(url):
    parsed = list(urlparse(url))
    soup = TakeUrls.takeHtmlContent(url)
    for image in soup.find_all("img"):
        # print("Image: %(src)s" % image)
        filename = image["src"].split("/")[-1]
        # print(image["src"])
        parsed[2] = image["src"]
        outpath = os.path.join("immagini", filename)
        if image["src"].lower().startswith("http"):
            urlretrieve(image["src"], outpath)
        else:
            urlretrieve(urlunparse(parsed), outpath)


print(takeImage("http://accessories.us.dell.com/sna/category.aspx?c=us&l=en&s=dhs&cs=19&category_id=2999&mfgpid=167691&chassisid=8499&stype=52&Tab=Parts"))

def takeCss(url):
    r = TakeUrls.takeHtmlContent(url)
    i=0
    for x in r.findAll('link', rel='stylesheet'):
        y = x['href']
        z = str(y)
        if z.startswith("http://") or z.startswith(("https://")):
            prova = TakeUrls.openUrl(z)
            file = open("prova" + str(i) + ".css", "w+")
            file.write(str(prova))
            file.close()
        elif z.startswith("//"):
            z = "http:"+z
            prova = TakeUrls.openUrl(z)
            file = open("prova" + str(i) + ".css", "w+")
            file.write(str(prova))
            file.close()
        elif not z.startswith("//"):
            z = "http://"+z
            prova = TakeUrls.openUrl(z)
            file = open("prova" + str(i) + ".css", "w+")
            file.write(str(prova))
            file.close()
        i = i+1
import requests
import bs4


def takeUrl(url):
    def prendiLista():
        listaFile = os.listdir("/home/gianlorenzo/AGIW/notebook/aliexpress.com")
        j = 0
        listaFile.remove("index.txt")
        for file in listaFile:
            f = codecs.open("/home/gianlorenzo/AGIW/notebook/aliexpress.com/" + file, 'r')
            html = (f.read())
            soup = bs4.BeautifulSoup(html, "lxml")
            o = []
            for l in soup.find_all("span"):
                o.append(l.text.strip())
        i = 0
        dict = {}
        while (i < len(o) - 1):
            dict[o[i]] = o[i + 1]
            i = i + 2
        file = open(str(j) + ".json", "w+")
        json.dump(dict, file)
        file.close()
        (print("ho scritto il file:" + str(j) + ".json"))
        j = j + 1


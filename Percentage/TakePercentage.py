import os
def checkDir(dir):
    # print(len([name for name in os.listdir(dir) if os.path.isfile(os.path.join(dir, name))]))
    return (len(os.listdir(dir)))

def getTotalDirectoryWithHtml(url):
    listaDir = os.listdir(url)
    i = 0
    for dir in listaDir:
        if not checkDir(url+dir)==1:
            i = i+1
    print("Le cartelle con html sono " + str(i) + " su " + str(checkDir(url)))

getTotalDirectoryWithHte
tml("/home/gianlorenzo/AGIW/notebook/")
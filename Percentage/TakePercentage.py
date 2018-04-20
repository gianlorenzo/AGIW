import os
def checkDir(dir):
    # print(len([name for name in os.listdir(dir) if os.path.isfile(os.path.join(dir, name))]))
    return (len(os.listdir(dir)))

def getTotalDirectoryWithHtml(url):
    listaDir = os.listdir(url)

    len = 0
    numDir=0
    for dir in listaDir:
        len = len + checkDir(url+dir)
        numDir = numDir+1
    print(str(len))
    print(str(numDir))


getTotalDirectoryWithHtml("/home/gianlorenzo/AGIW/JSONSTEP1(4)/")
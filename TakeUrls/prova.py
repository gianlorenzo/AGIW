import os

dirInputNotebook = "/home/davben/AGIW/notebook"
dirGlobaleDav = "/home/davben/AGIW/occurrence-extractor"
dirOutputGlobaleDav="/home/davben/AGIW/Step1/"
comandoDir="cd "+dirGlobaleDav
comandoClassifier="python2.7 -m src.model.specificationextractor "

listadir = os.listdir(dirInputNotebook)
def prova():
    os.system(comandoDir)
    os.system("mkdir X")
    os.system(comandoClassifier+"http://bestgamingpcreview.com/razer-blade-14-inch-touchscreen-gaming-laptop-512gb-windows-8-1-nvidia-geforce-gtx-870m"+dirGlobaleDav)

prova()
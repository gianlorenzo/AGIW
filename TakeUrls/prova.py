import os

def prova():
    os.chmod("/home/gianlorenzo",755)
    os.system("python2.7 -m src.model.specificationextractor http://gosale.com/5815969/lenovo-ideapad-yoga-13-multi merialdo")

prova()
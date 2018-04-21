#come feature scelgo i tag dell html rilevanti
#il target sara' il tag esatto che contiene le specifiche

import pandas as pd
import os

folderTrainDir = "/home/davben/Scrivania/FolderTrain"

def createMatrixTagger(folderTrainDir):
    matrixFeature = pd.DataFrame(columns = ["title","table","ul","target"])
    for dominio in os.listdir(folderTrainDir):
        for html in os.listdir(folderTrainDir+"/"+dominio):
            titleFile = open(folderTrainDir+"/"+dominio+"/"+html+"/"+"title.txt","r")
            titleFeat = titleFile.read()
            titleFile.close()
            tableFile = open(folderTrainDir+"/"+dominio+"/"+html+"/"+"table.txt","r")
            tableFeat = tableFile.read()
            tableFile.close()
            ulFile = open(folderTrainDir+"/"+dominio+"/"+html+"/"+"ul.txt","r")
            ulFeat = ulFile.read()
            ulFile.close()
            #    structFeat = open()
            targetFile = open(folderTrainDir+"/"+dominio+"/"+html+"/"+"target.txt","r")
            targetFeat = targetFile.read()
            targetFile.close()
            matrixFeature.loc[len(matrixFeature)]=[titleFeat,tableFeat,ulFeat,targetFeat]

    return matrixFeature

print(createMatrixTagger(folderTrainDir))
import os

def listOfFiles(directory, extension):
    filesNames=[]
    for file in os.listdir(directory):
        if file.endswith(extension):
            filesNames.append(file)
    return filesNames

def listPresident():
    filesNames=listOfFiles(".\speeches","txt")
    presidents= {}
    for file in filesNames:
        president=file.split("_")[1][:-4]
        for car in president :
            if car.isdigit():
                president=president.replace(car,"")
        if president not in presidents:
            presidents[president]=""
    return presidents

def fichiersToMin():
    filesNames=listOfFiles(".\speeches","txt")
    for file in filesNames:
        with open(".\speeches\\"+file,"r",encoding="utf-8") as speech:
            speechTexte=speech.read()
            speechTexte=speechTexte.lower()

        with open(".\cleaned\\"+file,"w",encoding="utf-8") as speech:
            speech.write(speechTexte)

def cleanFile():
    filesNames=listOfFiles(".\cleaned","txt")
    for file in filesNames:
        with open(".\cleaned\\"+file,"r",encoding="utf-8") as speech:
            speechTexte=speech.read()
            speechTexte=speechTexte.replace(",","")
            speechTexte=speechTexte.replace(".","")
            speechTexte=speechTexte.replace("'"," ")
            speechTexte=speechTexte.replace('-'," ")
            speechTexte=speechTexte.replace('\n'," ")
        with open(".\cleaned\\"+file,"w",encoding="utf-8") as speech:
            speech.write(speechTexte)

def reloadTexte():
    filesNames = listOfFiles(".\speeches", "txt")
    for file in filesNames:
        with open(".\speeches\\" + file, "r",encoding="utf-8") as speech:
            speechTexte = speech.read()

        with open(".\cleaned\\" + file, "w",encoding="utf-8") as speech:
            speech.write(speechTexte)



import os

def listOfFiles(directory:str, extension:str):
    """Retourne une liste contenant les noms des fichiers du dossier "directory" ayant l'extension "extension"""
    filesNames=[]
    for file in os.listdir(directory):
        if file.endswith(extension):
            filesNames.append(file)
    return filesNames


def listPresident():
    """Retourne une liste des noms des présidents et les mets dans le dossier "speeches" """
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

def associerNomPrenom():
    """Associe les noms des president à leurs prenoms """
    nomPrenomPresident = {}
    for nomPresident in listPresident():
        if nomPresident == "Macron":
            nomPrenomPresident[nomPresident]="Emmanuel"
        elif nomPresident == "Hollande":
            nomPrenomPresident[nomPresident]="François"
        elif nomPresident ==  "Sarkozy":
            nomPrenomPresident[nomPresident]="Nicolas"
        elif nomPresident == "Chirac":
            nomPrenomPresident[nomPresident]="Jacques"
        elif nomPresident == "Mitterand":
            nomPrenomPresident[nomPresident]="François"
        elif nomPresident == "Giscard dEstaing":
            nomPrenomPresident[nomPresident]="Valerie"
    return nomPrenomPresident


def fichiersToMin():
    """Permet de convertir les 8 fichiers dans le dossiers speeches en minuscule et les enregistre dans le dossier cleaned"""
    filesNames=listOfFiles(".\speeches","txt")
    for file in filesNames:
        with open(".\speeches\\"+file,"r",encoding="utf-8") as speech:
            speechTexte=speech.read()
            speechTexte=speechTexte.lower()

        with open(".\cleaned\\"+file,"w",encoding="utf-8") as speech:
            speech.write(speechTexte)

def cleanFile():
    """Remplace ou suprime les caractères spéciaux et les sauts de lignes"""
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
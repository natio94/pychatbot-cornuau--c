from math import log
from fonctionsBase import *

def scoreTF(document:str):
    """Retourne un dictionnaire contenant les scores TF des mots du document"""
    freq = {}
    with open(".\cleaned" + "\\" + document, "r", encoding="utf-8") as speech:
        docu = speech.read()
        for mot in docu.split(" "):
            if mot not in freq:
                freq[mot] = 1
            else:
                freq[mot] += 1
    return freq

def scoreIDF(directory:str):
    """Retourne un dictionnaire contenant les scores IDF des mots du dossier directory"""
    freqInv = {}
    documents = listOfFiles(directory, "txt")
    for document in documents:
        with open(directory + "\\" + document, "r",encoding="utf-8") as speech:
            doc = speech.read()
            for mot in set(doc.split(" ")):
                if mot not in freqInv:
                    freqInv[mot] = 1
                else:
                    freqInv[mot] += 1
    for mot in freqInv.keys():
        freqInv[mot]=log(len(documents)/freqInv[mot])
    return freqInv


def matTF_IDF(directory:str):
    """Retourne une matrice contenant les fréquences TF-IDF des mots de chaque document du dossier et une list avec les mots dans le meme ordre que la matrice"""
    documents = listOfFiles(directory, "txt")
    matrice = []
    for document in documents:
            colonne = []
            freqInv=scoreIDF(directory)
            freq=scoreTF(document)
            for mot in freqInv.keys():
                if mot in freq.keys():
                    score=freq[mot]*freqInv[mot]
                else:
                    score=0
                colonne.append(score)
            matrice.append(colonne)
            listMot=list(freqInv.keys())
    return matrice,listMot


def motsMoinsImportants(directory):
    matrice, listMot = matTF_IDF(directory)
    mots_non_importants = []

    for i in range(len(listMot)):
        score_total = sum(matrice[j][i] for j in range(len(matrice)))
        if score_total==0:
            mots_non_importants.append(listMot[i])

    return mots_non_importants


def motPlusEleveTFIDF(directory:str):
    """Retourne un liste contenant le ou les mots ayant le score TF-IDF le plus élévé"""
    matrice, listMot = matTF_IDF(directory)
    mots_max_tfidf = []

    for i in range(len(listMot)):
        scores = [matrice[j][i] for j in range(len(matrice))]
        if max(scores) > 0:
            mots_max_tfidf.append((listMot[i], max(scores)))

    mots_max_tfidf.sort(key=lambda x: x[1], reverse=True)
    return mots_max_tfidf[0]


def presidentsParlantDeMot(directory:str, mot:str):
    """Retourne la liste des présidents parlant d'un mot donné et le président l'ayant dit le plus de fois'"""
    documents = listOfFiles(directory, "txt")

    presidents=listPresident()
    presidentsOccurrences = {president:0 for president in presidents}
    for i in range(len(documents)):
        document=documents[i]
        if i<=1:
            president = presidents[0]
        elif i<=4:
            president = presidents[i-1]
        elif i ==5:
            president=presidents[4]
        elif i>5:
            president=presidents[5]
        with open(directory + "\\" + document, "r", encoding="utf-8") as speech:
            docu=speech.read()
            if mot in document:
                presidentsOccurrences[president] += docu.count(mot)
        presToRemove=[]

    for pres in presidentsOccurrences:
        if presidentsOccurrences[pres] == 0:
            presToRemove.append(pres)
    for pres in presToRemove:
        presidentsOccurrences.pop(pres)
    presidentsOccurrences1 = sorted(presidentsOccurrences.items(), key=lambda x: x[1], reverse=True)

    return list(presidentsOccurrences.keys()),presidentsOccurrences1[0][0]



def premierPresidentParlantDeMots(directory:str, mots:list):
    """Retourne le premier président parlant d'une list de mot donnée"""
    documents = listOfFiles(directory, "txt")
    ordrePresChrono = ["Giscard dEstaing", "Mitterand", "Chirac", "Sarkozy", "Hollande", "Macron"]
    president = []
    for document in documents:
        with open(directory + "\\" + document, "r", encoding="utf-8") as speech:
            docu = speech.read()
            if any(mot in docu for mot in mots):
                presDit.append(president)
    for pres in ordrePresChrono:
        if pres in presDit:
            return pres

def motsEvoquesParTous():
    """Retourne la liste des mots évoqués par tous les présidents"""
    matrice,listeMot=matTF_IDF("./cleaned")
    mots=[]
    for i in range(len(listeMot)):
        if (matrice[0][i]!=0 or matrice[1][i]!=0) and matrice[2][i]!=0 and matrice[3][i]!=0 and matrice[4][i]!=0 and (matrice[5][i]!=0 or matrice[6][i]!=0):
            mots.append(listeMot[i])
    return mots

def motsPlusRepetesChirac():
    freq1 = scoreTF("Nomination_Chirac1.txt")
    freq2 = scoreTF("Nomination_Chirac2.txt")
    freq3 = {}

    for mot in freq1.keys():
        if mot in freq2.keys():
            freq3[mot] = freq1[mot] + freq2[mot]
    motsPlusRepetes=[]
    maxScore=0
    for mot in freq3.keys():
        score = freq3[mot]
        if maxScore < score:
            maxScore = score
            motsPlusRepetes = [mot]
        elif maxScore == score:
            motsPlusRepetes.append(mot)

    return motsPlusRepetes
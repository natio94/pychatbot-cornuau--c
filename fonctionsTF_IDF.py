from math import log
from fonctionsBase import *

def scoreTF(document:str):
    """Retourne un dictionnaire contenant les scores TF des mots du document"""
    freq = {}
    with open(".\cleaned" + "\\" + document, "r", encoding="utf-8") as speech:
        doc = speech.read()
        for mot in doc.split(" "):
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
            for mot in doc.split(" "):
                if mot not in freqInv:
                    freqInv[mot] = 1
                else:
                    freqInv[mot] += 1
    for mot in freqInv.keys():
        freqInv[mot]=log(len(documents)/freqInv[mot]+1)
    return freqInv


def matTF_IDF(directory:str):
    """Retourne une matrice contenant les fréquences TF-IDF des mots de chaque document du dossier et une list avec les mots dans le meme ordre que la matrice"""
    documents = listOfFiles(directory, "txt")
    matrice = []
    for document in documents:
        with open(directory + "\\" + document, "r",encoding="utf-8") as speech:
            doc = speech.read()
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
        if score_total == 0:
            mots_non_importants.append(listMot[i])

    return mots_non_importants


def motPlusElevéTFIDF(directory):
    matrice, listMot = matTF_IDF(directory)
    mots_max_tfidf = []

    for i in range(len(listMot)):
        scores = [matrice[j][i] for j in range(len(matrice))]
        if max(scores) > 0:
            mots_max_tfidf.append((listMot[i], max(scores)))

    mots_max_tfidf.sort(key=lambda x: x[1], reverse=True)
    return mots_max_tfidf


def presidentsParlantDeNation(directory, mot="nation"):
    documents = listOfFiles(directory, "txt")
    presidents_occurrences = {}

    for document in documents:
        with open(directory + "\\" + document, "r", encoding="utf-8") as speech:
            doc = speech.read().lower()
            if mot in doc:
                president = document.split("_")[1][:-4]
                if president not in presidents_occurrences:
                    presidents_occurrences[president] = doc.count(mot)

    presidents_occurrences = sorted(presidents_occurrences.items(), key=lambda x: x[1], reverse=True)
    return presidents_occurrences


def premierPresidentParlantDeClimatEcologie(directory, mots=["climat", "écologie"]):
    documents = listOfFiles(directory, "txt")

    for document in documents:
        with open(directory + "\\" + document, "r", encoding="utf-8") as speech:
            doc = speech.read().lower()
            if any(mot in doc for mot in mots):
                president = document.split("_")[1][:-4]
                return president

def motsEvoquesParTous(directory, mots_non_importants):
    documents = listOfFiles(directory, "txt")
    mots_evoques_tous = set()

    for document in documents:
        with open(directory + "\\" + document, "r", encoding="utf-8") as speech:
            doc = speech.read().lower().split()

            mots_evoques_tous.update(set(doc) - set(mots_non_importants))

    return list(mots_evoques_tous)

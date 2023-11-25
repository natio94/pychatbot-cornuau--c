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


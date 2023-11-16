from math import log
from fonctionsBase import *
def frequence(directory):
    """Retourne un dictionnaire contenant les fréquences des mots du document"""
    freq = {}
    documents = listOfFiles(directory, "txt")
    for document in documents:
        with open(directory+"\\"+document,"r",encoding="utf-8") as speech:
            doc=speech.read()
            for mot in doc.split(" "):
                if mot not in freq:
                    freq[mot] = 1
                else:
                    freq[mot] += 11
    return freq

def frequence_inverse(directory):
    freq=frequence(directory)
    freqInv={}
    for mot in freq.keys():
        freqInv[mot]=log(8/freq[mot])
    return freqInv

def tf_idf(directory):
    freq=frequence(directory)
    freqInv=frequence_inverse(directory)
    tfidf={}
    for mot in freq.keys():
        tfidf[mot]=freq[mot]*freqInv[mot]
    return tfidf

def matTF_IDF(directory):
    documents = listOfFiles(directory, "txt")
    matrice = []
    for document in documents:
        with open(directory + "\\" + document, "r",encoding="utf-8") as speech:
            doc = speech.read()
            tf_idfMot= tf_idf(directory)
            ligne = [mot for mot in tf_idfMot.keys()]
            for mot in doc.split(" "):
                ligne.append(tf_idfMot[mot])
            matrice.append(ligne)
    return matrice
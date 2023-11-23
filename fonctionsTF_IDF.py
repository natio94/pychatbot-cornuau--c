from math import log
from fonctionsBase import *
def frequence(directory:str):
    """Retourne un dictionnaire contenant les fréquences TF des mots du document"""
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

def frequence_inverse(directory:str):
    """Retourne un dictionnaire contenant les fréquences inverses IDF des mots du document"""
    freq=frequence(directory)
    freqInv={}
    for mot in freq.keys():
        freqInv[mot]=log(8/freq[mot])
    return freqInv

def tf_idf(directory:str):
    """Retourne un dictionnaire contenant les fréquences TF-IDF des mots du document soit le produit des fréquences TF et IDF"""
    freq=frequence(directory)
    freqInv=frequence_inverse(directory)
    tfidf={}
    for mot in freq.keys():
        tfidf[mot]=freq[mot]*freqInv[mot]
    return tfidf

def matTF_IDF(directory:str):
    """Retourne une matrice contenant les fréquences TF-IDF des mots de chaque document du dossier et une list avec les mots dans le meme ordre que la matricela fonction"""
    documents = listOfFiles(directory, "txt")
    matrice = []
    for document in documents:
        with open(directory + "\\" + document, "r",encoding="utf-8") as speech:
            doc = speech.read()
            tf_idfMot= tf_idf(directory)
            ligne = [mot for mot in tf_idfMot.keys()]
            listMot=list(tf_idfMot.keys())
    return matrice,listMot




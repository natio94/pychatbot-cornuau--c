from fonctionsTF_IDF import *
from fonctionsBase import *
from math import *
def tokenQuestion(question):
    """Retourne la liste des mots de la question sans les caractères spéciaux"""
    question = question.replace(",", "")
    question = question.replace(".", "")
    question = question.replace("'", " ")
    question = question.replace('-', " ")
    question = question.replace('\n', " ")
    question = question.lower()
    question = question.split()
    return question

def recherche(liste,directory):
    """Retourne la liste des mots de la question qui sont dans le corpus"""
    listMot=matTF_IDF(directory)[1]
    motDansCorpus=[]
    for mot in liste:
        if mot in listMot:
            motDansCorpus.append(mot)
    return motDansCorpus

def vectorisation(liste):
    """Retourne le vecteur TFIDF de la question"""
    tfMot=[]
    idfMot=[]
    tfidfMot=[]
    listeSet=list(dict.fromkeys(liste))
    mat, listeMot = matTF_IDF("./cleaned")
    for mot in listeSet :
        tfMot.append(liste.count(mot))
        pos=listeMot.index(mot)
        somme=0
        for i in range(len(mat)):
            somme+=mat[i][pos]
        idfMot.append(somme/len(mat))
    for mot in listeMot:
        if mot in listeSet :
            pos=listeSet.index(mot)
            tfidfMot.append(idfMot[pos]*tfMot[pos])
        else:
            tfidfMot.append(0)
    return tfidfMot

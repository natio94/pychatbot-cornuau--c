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

def prodScalaire(vecteurQuestion,mat):
    """Retourne le produit scalaire entre le vecteur de la question et les vecteurs des documents"""
    prod=[]
    for i in range(len(mat)):
        res = 0
        doc=mat[i]
        for j in range(len(vecteurQuestion)):
            res+=vecteurQuestion[j]*doc[j]
        prod.append(res)
    return prod

def norme(vecteur):
    """Retourne la norme du vecteur"""
    somme=0
    for nb in vecteur:
        somme+=nb**2
    return sqrt(somme)

def similarite(vecteurQuestion,mat):
    """Retourne le calcul de la similarité entre le vecteur de la question et les vecteurs des documents"""
    prod=prodScalaire(vecteurQuestion,mat)
    res=[]
    for i in range(len(prod)):
        res.append(prod[i]/(norme(vecteurQuestion)*norme(mat[i])))
    return res

def calculDocPertinent(mat,vecteurQ,nomsDoc):
    """Retourne le nom du document le plus pertinent grace au calcul de la similarité"""
    sim=similarite(vecteurQ,mat)
    return maxi2Liste(sim,nomsDoc)

def maxi2Liste(liste1,liste2):
    """retourne le nom de l'element de la liste2 associé au maximum de la liste1"""
    maxi=liste1[0]
    pos=0
    for i in range(1,len(liste1)):
        if liste1[i]>maxi:
            maxi=liste1[i]
            pos=i
    return liste2[pos]

def genRep(question):
    """Generer une réponse à la question"""
    mat,listeMot=matTF_IDF("./cleaned")
    clean=recherche(tokenQuestion(question),"./cleaned")
    vecteur=vectorisation(clean)
    nomsDoc=listOfFiles("./cleaned","txt")
    docu=calculDocPertinent(mat,vecteur,nomsDoc)
    motMax = maxi2Liste(vecteur, listeMot)
    with open("./speeches/"+docu,"r",encoding="utf-8") as speech:
        speechTexte=speech.read()
        speechTexte=speechTexte.split(".")
        for phrase in speechTexte:
            if motMax in phrase:
                return phrase
        return "Je ne sais pas répondre à cette question"

def affinageRep(question):
    """Affine la réponse à la question avec une phrase d'introduction et une correction de la ponctuation"""
    rep=genRep(question)
    rep=rep.replace("\n","")
    rep = rep[0].lower() + rep[1:]
    if rep[-1]!=".":
        rep+="."
    questionStarter={"Comment":"Après analyse","Pourquoi":"Car","Quand":"En","Où":"Dans","Qui":"C'est","Quel":"C'est","Quelle":"C'est"}
    if question.split(" ")[0] in questionStarter.keys():
        rep = questionStarter[question.split(" ")[0]] + " " + rep
    rep = rep[0].upper() + rep[1:]
    return rep

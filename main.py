
rep=input("Quel fonction voulez vous utiliser ?\n1:fonctions de base\n2:fonctions TF_IDF\n")
#fonctions de base
if rep=="1":
    from fonctionsBase import *
    rep=input("Que voulez vous faire ?\n1:Liste des présidents\n2:Associer nom et prénom\n3:Convertir les fichiers en minuscule\n4:Nettoyer les fichiers\n")
    if rep=="1":
        print(listPresident())
    elif rep=="2":
        print(associerNomPrenom())
    elif rep=="3":
        fichiersToMin()
    elif rep=="4":
        cleanFile()

#fonctions TF_IDF
elif rep=="2":
    from fonctionsTF_IDF import *
    rep=input("Que voulez vous faire ?\n1:Mots les moins importants\n2:Mot avec le score TF-IDF le plus élevé\n3:Présidents parlant d'un mot\n4:Premier président parlant de mots\n5:Mots évoqués par tous\n")
    if rep=="1":
        print(motsMoinsImportants("./cleaned"))
    elif rep=="2":
        print(motPlusEleveTFIDF("./cleaned"))
    elif rep=="3":
        mot=input("Quel mot voulez vous chercher ?\n")
        print(presidentsParlantDeMot("./cleaned",mot))
    elif rep=="4":
        mots=[]
        nbMots=int(input("Combien de mots voulez vous chercher ?\n"))
        for i in range(nbMots):
            mots.append(input("Quel mot voulez vous chercher ?\n"))
        print(premierPresidentParlantDeMots("./cleaned",mots))
    elif rep=="5":
        print(motsEvoquesParTous())
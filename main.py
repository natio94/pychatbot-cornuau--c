from fonctionsBase import *
#print(listOfFiles(".\speeches","txt"))
#print(listPresident())
reloadTexte()
fichiersToMin() #ne marche pas car lower cause des problèmes avec les accents (encodage)
 #pour retester les fonctions de modification des fichiers
cleanFile()

#with open(".\cleaned\\Nomination_Macron.txt","r") as speech:
#speechTexte=speech.read()


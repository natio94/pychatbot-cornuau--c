from fonctionsBase import *
from fonctionsTF_IDF import *
#print(listOfFiles(".\speeches","txt"))
#print(listPresident())
reloadTexte()
fichiersToMin() #ne marche pas car lower cause des problèmes avec les accents (encodage)
 #pour retester les fonctions de modification des fichiers
cleanFile()

#with open(".\cleaned\\Nomination_Macron.txt","r") as speech:
#speechTexte=speech.read()
print(frequence(".\cleaned"))

#print(frequence_inverse(".\cleaned"))

#print(max(tf_idf(".\cleaned").items()), lambda x: x[1])

#print(matTF_IDF(".\cleaned")[0:2])

from fonctionsBase import *
from fonctionsTF_IDF import *


print(motsMoinsImportants(".\cleaned"))

print(motPlusEleveTFIDF(".\cleaned"))

print(motsPlusRepetesChirac())

print(presidentsParlantDeMot(".\cleaned","nation"))
print(listPresident())

print(premierPresidentParlantDeMots(".\cleaned",["écologie","climat"]))

print(motsEvoquesParTous())



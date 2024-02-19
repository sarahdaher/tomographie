import time
import sys
from constantes import *
from grille import *
from lecture import *
from colorierCase import *
from resolution import *

""" 
#tests
s = [1, 2, 2] 
l = 3  #taille de s
j = 7
res = ColoriagePossibleLigneOuCol(j-1, l, s)
print(res)


#tests
s = [5] 
l = 1 #taille de s
j = 7
tab = [3,3,3,2,3,1,3]
T = initialiserTab2Dim(j,l+1,VIDE)
res = ColoriagePossibleLigneOuColPreremplie(T, tab ,j-1, l, s)
#print(res)


#pour obtenir les temps d'execution par propagation

for i in range(0, 11):
  chiffre = str(i)
  start = time.time()
  propagation("instances/"+chiffre+".txt")
  end = time.time()
  duree = end - start
  print("pour l'instance ", i, " le temps d'execution est de ", duree, " secondes")

#pour obtenir les temps d'execution par enumeration

for i in range(0, 17):
  chiffre = str(i)

  start = time.time()
  resolutionComplete("instances/"+chiffre+".txt")
  end = time.time()
  duree = end - start
  print("pour l'instance ", i, " le temps d'execution est de ", duree, " secondes")

"""
instance = input("Entrez le numéro de l'instance : ")

if int(instance)<0: 
  print("Erreur : Numéro d'instance incorrect")
  sys.exit()
  
algo =  input("Quel algorithme vouliez-vous appliquer sur l'instance? \nTapez p pour propagation et e pour enumeration : ")

start = time.time()

if algo == "p":
  propagation("instances/"+instance+".txt")
elif algo == "e":
  resolutionComplete("instances/"+instance+".txt")
else:
  print("Erreur : algorithme inconnu")
  sys.exit()

end = time.time()
duree = end - start

print("pour l'instance ", instance, " le temps d'execution est de ", duree, " secondes")

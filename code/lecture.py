from constantes import *
from grille import *

#tranformer les fichiers.txt en grille
def fichierToGrille(fileTxt):
   f = open(fileTxt, "r")
   sL = [] #sequences lignes
   sC=[] #sequenes colonnes
   colonne = False
  
   for ligne in f:
     
     if ligne != "": 
       if ligne == "#\n": #on croise le séparateur entre les lignes et les colonnes
         colonne = True
         continue
         
       if colonne:
         lC = [int(x) for x in (ligne.strip()).split()] #la methode .strip() permet d'ignorer les espaces tout à gauche et tout à droite de la ligne ; la methode .split() crée une liste des éléments de la ligne (car le separateur par defaut est l'espace)
         sC+= [lC]
         
       else: #c'est une ligne
         lL = [int(x) for x in (ligne.strip()).split()]
         sL+= [lL]
         
   G = initialiserTab2Dim(len(sL), len(sC), PASCOLORE) #len(sL) = nb de lignes ; len(sC) = nb de colonnes
   return (G, sL, sC)

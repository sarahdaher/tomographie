from constantes import *

"""FONCTIONS EN RAPPORT AVEC LA GRILLE REPRESENTEE PAR UNE MATRICE"""

#initialise un tableau a 2 dimensions (grille) de n lignes et m colonnes avec val
def initialiserTab2Dim(n,m,val):
  return [[val for _ in range(m)] for _ in range(n)]

#retourne la k eme colonne de la matrice, afin de l'avoir sous forme de liste
def colonneKDansG(G, k):  
  C = []
  for i in range(len(G)):
    C.append(G[i][k])
  return C

#teste si la matrice M est entierement coloriee
def MatriceColorie(M):
  for i in range(len(M)):
    for j in range(len(M[i])):
      if M[i][j] == PASCOLORE:
        return False
  return True

#affichage de la grille coloriee
def AfficherMatriceCouleur(M) :
  for i in range(len(M)):
    for j in range(len(M[i])):
      if M[i][j] == NOIR:
        print(noir, end="")
        
      elif M[i][j] == BLANC:
        print(blanc, end="")
        
      else:
        print(jaune, end="")
    print()
  return
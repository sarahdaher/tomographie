from constantes import *
from grille import *


""" USAGE DE LA PROGRAMMATION DYNAMIQUE"""

#question 4: coloriage possible d'une ligne incolore avec une sequence donnée
#APPEL INITIAL : j = M-1 avec M la taille de la ligne ou colonne consideree, s la sequence donnee (liste), l=len(s),
# memoization_dict : dictionnaire de memoisation dans lequel on va stocker les valeurs des appels de la fonction :  memoization_dict[(j, l)] contiendra la valeur de retour de l'appel  ColoriagePossibleLigneOuCol( j, l, s, memoization_dict) une fois celui-ci terminé.
def ColoriagePossibleLigneOuCol(j, l, s,  memoization_dict= {}):

  if (j, l) in memoization_dict:#si stockée dans le tableau de mémoïsation (alors déjà calculée)
      return memoization_dict[(j, l)]
  
  elif l == 0: #cas1 si pas de bloc -> vrai
    memoization_dict[(j, l)] = True
    
  elif l >= 1 and j < s[l-1] - 1: #cas2a si pas de place et au moins un bloc -> faux
    memoization_dict[(j, l)] = False
    
  elif l>=1 and j == s[l-1]-1: #cas2b si place que pour 1 bloc, et au moins un bloc -> vrai ssi on n'a qu'un bloc (ssi l=1)
    memoization_dict[(j, l)]= (l==1)
    
  elif l>=1 and j >s[l-1] - 1: #cas2c si place au moins pour le dernier bloc, et au moins un bloc -> on teste si c'est vrai en coloriant la case en blanche ou en coloriant sl cases en noir (correspondant au dernier bloc) et une case de transition en blanc
    memoization_dict[(j, l)] = ColoriagePossibleLigneOuCol(j-1, l, s, memoization_dict) or ColoriagePossibleLigneOuCol(j-s[l-1]-1, l-1, s, memoization_dict)
    
  else:
    print("Erreur parametres")
    return False
  return memoization_dict[(j, l)]


#question 5: coloriage possible d'une ligne ou colonne contenant des cases deja coloriees avec une sequence donnée

#teste si val n'est pas present entre i1 et i2 inclus
def NonPresenceValeur(tab, i1, i2, val):
  for i in range(i1,i2+1) :
    if tab[i] ==val :
      return False
  return True

#APPEL AVEC :
#j = M-1 avec M la taille de la ligne ou colonne consideree, s la sequence donnee (liste), l=len(s), memoization_dict un dictionnaire de memoisation vide
#tab: tableau de taille j contenant le statut de la coloration de la ligne ou colonne.
#memoization_dict : dictionnaire de memoisation dans lequel on va stocker les valeurs des appels de la fonction : memoization_dict[(j,l)] contiendra la valeur de retour de l'appel  ColoriagePossibleLigneOuColPreremplie(tab,j,l,s, memoization_dict) une fois celui-ci terminé. 
def ColoriagePossibleLigneOuColPreremplie(tab, j, l, s, memoization_dict= {}):
    if (j, l) in memoization_dict:
        return memoization_dict[(j, l)]

    elif l == 0:  # cas1
        memoization_dict[(j, l)] = NonPresenceValeur(tab, 0, j, NOIR)

    elif l >= 1 and j < s[l - 1] - 1:  # cas 2a
        memoization_dict[(j, l)] = False

    elif l > 1 and j == s[l - 1] - 1:  # cas 2b avec l>1
        memoization_dict[(j, l)] = False

    elif l == 1 and j == s[l - 1] - 1:  # cas 2b avec l = 1
        memoization_dict[(j, l)] = NonPresenceValeur(tab, 0, j, BLANC)

    elif l >= 1 and j > s[l - 1] - 1:  # cas 2c
        #avant le or: il faut que tab[j] ne soit pas noire (devra etre blanche) et on teste si la sequence s entre dans les j-1 premieres cases.
        #apres le or: il faut que tab[j] ne soit pas blanche (devra etre noire) et qu'il n'y ait pas de blanc qui couvre le dernier bloc (sl) a positionner a la fin (vu qu'il sera colorie en noir) et que la case precedant sl ne soit pas noire (elle devra etre blanche sinon la sequence sera plus longue). Une fois sl positionne, on teste si la sequence s\{sl} entre dans les j-sl-1  premieres cases. 
        #ce qui donne la formule suivante
        memoization_dict[(j, l)] = (
            (tab[j] != NOIR and ColoriagePossibleLigneOuColPreremplie(tab, j - 1, l, s, memoization_dict)) or
            (tab[j] != BLANC and NonPresenceValeur(tab, j - s[l - 1] + 1, j, BLANC) and tab[j - s[l - 1]] != NOIR and
             ColoriagePossibleLigneOuColPreremplie(tab, j - s[l - 1] - 1, l - 1, s, memoization_dict))
        )

    else:
        print("Erreur parametres")
        return False

    return memoization_dict[(j, l)]

from colorierCase import *
from grille import *
import copy
from lecture import *

################################## PARTIE 1 #################################
# RESOLUTION INCOMPLETE


def ColoreLig(G, k, s, nouveaux):  #colorie la ligne G[k] avec la sequence s
  L = copy.deepcopy(G[k])
  M = len(L)
  j = M - 1
  l = len(s)
  for i in range(M):

    if L[i] == PASCOLORE:  #on teste si on peut colorier L[i]

      L[i] = BLANC
      test_blanc = ColoriagePossibleLigneOuColPreremplie(L, j, l, s, {})  #test si on peut la colorier en blanc

     
      L[i] = NOIR
      test_noir = ColoriagePossibleLigneOuColPreremplie(L, j, l, s, {})  #test si on peut la colorier en noir

      L[i] = PASCOLORE  #on remet L[i] sans couleur apres avoir teste

      if (not test_noir and not test_blanc):
        return ( False, G)  # pas de solution pour le puzzle si on ne peut colorier la case ni en blanc ni en noir
      elif (test_noir and not test_blanc):  #on la colorie en noir si elle peut etre uniquement noire
        L[i] = NOIR
        G[k][i] = NOIR
        nouveaux.add(i)  #ajouter la colonne dans nouveaux si elle ne l'est pas deja

      elif (test_blanc and not test_noir):  #on la colorie en blanc si elle peut etre uniquement blanche
        L[i] = BLANC
        G[k][i] = BLANC
        nouveaux.add(i)  #ajouter la colonne dans nouveaux si elle ne l'est pas deja

      #si elle peut etre blanche ou noir on ne fait rien !
    
    else: #si la case etait déjà coloriée on vérifie que ce coloriage est valide
      test = ColoriagePossibleLigneOuColPreremplie(L, j, l, s, {})  
      if not test:
        return (False, G)
        
  return (True, G)


def ColoreCol(G, k, s,nouveaux):  #colorie la colonne k de la grille G avec la sequence s
  C = colonneKDansG(G, k)  #extraire la colonne k de G
  N = len(C)
  j = N - 1
  l = len(s)

  for i in range(N):
    if C[i] == PASCOLORE:  #on teste si on peut colorier C[i]
  
      C[i] = BLANC
      test_blanc = ColoriagePossibleLigneOuColPreremplie(C, j, l, s, {})  #test si on peut la colorier en blanc

      C[i] = NOIR
      test_noir = ColoriagePossibleLigneOuColPreremplie(C, j, l, s, {})  #test si on peut la colorier en noir

      C[i] = PASCOLORE  #on remet C[i] sans couleur apres avoir teste

      if (not test_noir and not test_blanc):
        return (False, G)  # pas de solution pour le puzzle si on ne peut colorier la case ni en blanc ni en noir

      elif (test_noir and not test_blanc):  #on la colorie en noir si elle peut etre uniquement noire
        C[i] = NOIR
        G[i][k] = NOIR
        nouveaux.add(i)  #ajouter la ligne i correspondante dans nouveaux si elle ne l'est pas deja

      elif (test_blanc and not test_noir):  #on la colorie en blanc si elle peut etre uniquement blanche
        C[i] = BLANC
        G[i][k] = BLANC
        nouveaux.add(i)  #ajouter la ligne i correspondante dans nouveaux si elle ne l'est pas deja

      #si elle peut etre blanche ou noire on ne fait rien !
      
    else:
      test = ColoriagePossibleLigneOuColPreremplie(C, j, l, s, {})  #si la case etait déjà coloriée on vérifie que ce coloriage est valide
      if not test:
        return (False, G)
        
  return (True, G)


def coloration(A, sL, sC):  #len(sL) = len(A), len(sC) = len(A[0])

  G = copy.deepcopy(A)
  N = len(G)  #nb de lignes
  M = len(G[0])  #nb de colonnes

  lignesAvoir = set(i for i in range(N))
  colonnesAvoir = set(i for i in range(M))

  while (lignesAvoir != set() or colonnesAvoir != set()):

    for i in set(lignesAvoir):
      nouveaux = set()
      (ok, G) = ColoreLig(G, i, sL[i], nouveaux)
      if not ok:
        return ("VRAI", initialiserTab2Dim(N, M, PASCOLORE))  #Si c'est faux on retourne la matrice vide

      colonnesAvoir = colonnesAvoir | nouveaux  #on ajoute les nouvelles colonnes à traiter s'il y a eu modification dans la grille apres ColoreLig
      lignesAvoir.remove(i)  #on a traite la ligne i donc on la retire de la liste des lignes à traiter

    for j in set(colonnesAvoir):
      nouv = set()
      (ok2, G) = ColoreCol(G, j, sC[j], nouv)
      if not ok2:
        return ("FAUX", initialiserTab2Dim(N, M, PASCOLORE))  #Si c'est faux on retourne la matrice vide

      lignesAvoir = lignesAvoir | nouv
      colonnesAvoir.remove(j)

  if MatriceColorie(G):  #toutes les cases sont coloriées en blanc ou en noir donc on a une solution au puzzle
    return ("VRAI", G)
  else:  #il existe des cases non coloriées
    return ("NESAITPAS", G)  #on ne peut pas conclure


#algorithme de propagation (lecture du fichier .txt -> appliquer l'algo de coloration -> visualiser la grille coloriee)
def propagation(fichier):
  G, sL, sC = fichierToGrille(fichier)
  (ok, G1) = coloration(G, sL, sC)
  print(ok)
  AfficherMatriceCouleur(G1)


################################## PARTIE 2 #################################
#  RESOLUTION COMPLETE


def colorierEtPropager(G, sL, sC, i, j, c):  #len(sL) = len(A), len(sC) = len(A[0])

  lignesAvoir = {i}
  colonnesAvoir = {j}

  G[i][j] = c  #on colorie la case (i,j) avec la couleur c

  while (lignesAvoir != set() or colonnesAvoir != set()):

    for i in set(lignesAvoir):
      nouveaux = set()
      (ok, G) = ColoreLig(G, i, sL[i],nouveaux)  #essaye de colorier la ligne i
      if not ok:
        return ("FAUX", initialiserTab2Dim(len(G), len(G[0]), PASCOLORE))  #Si c'est faux on retourne la matrice vide
      colonnesAvoir = colonnesAvoir | nouveaux  #on met a jour la liste des colonnes à traiter
      lignesAvoir.remove(i)  #on a traite la ligne i donc on la retire de la liste des lignes a traiter

    for j in set(colonnesAvoir):
      nouv = set()
      (ok2, G) = ColoreCol(G, j, sC[j], nouv)  #essaye de colorier la colonne j
      if not ok2:
        return ("FAUX", initialiserTab2Dim(len(G), len(G[0]), PASCOLORE))  #Si c'est faux on retourne la matrice vide
      lignesAvoir = lignesAvoir | nouv  #on met a jour la liste des lignes à traiter
      colonnesAvoir.remove(j)  #on a traite la colonne j donc on la retire de la liste des colonnes a traiter

  if MatriceColorie( G):  #si la grille est est entierement coloriee alors on a une solution
    return ("VRAI", G)
  else:
    return ("NESAITPAS", G)  #sinon on ne peut pas conclure


#trouve la prochaine case indeterminee a partir de la case k
def trouverProchaineCaseIndeterminee(k, M, N, A):
  i = k // M
  j = k % M
  #on a les indices (i,j) correspondant a k
  for o in range(i, N):
    for m in range(j, M):
      if A[o][m] == PASCOLORE:
        return M * o + m
  return M * N


def enumRec(A, sL, sC, k, c):
  N = len(A)  #nb de lignes
  M = len(A[0])  #nb de colonnes
  if k == M * N:
    return ("VRAI", A)  #toutes les cases sont determinees -> on retourne la grille coloriee
  #on extrait (i,j) de k
  i = k // M
  j = k % M
  (ok, G) = colorierEtPropager(A, sL, sC, i, j, c)  #on essaye de colorier la premiere case indeterminee (i,j) avec la couleur c

  if ok == "FAUX":
    return ("FAUX", initialiserTab2Dim(len(A), len(A[0]), PASCOLORE))  #retourne la matrice vide si c'est faux
  elif ok == "VRAI":
    return ("VRAI", G)  #retourne la grille coloriee si c'est vrai
  else:
    G_copy = copy.deepcopy(G)
    k2 = trouverProchaineCaseIndeterminee(
        k + 1, M, N, G)  #on cherche la prochaine case indeterminee
    (ok1, G1) = enumRec(G_copy, sL, sC, k2,BLANC)  #on essaye de la colorier en blanc

    #si c'est vrai, c'est une solution !
    if ok1 == "VRAI":
      return ("VRAI", G1)

    (ok2, G2) = enumRec(G, sL, sC, k2, NOIR)  #on essaye de la colorier en noir

    #si c'est vrai, c'est une solution !
    if ok2 == "VRAI":
      return ("VRAI", G2)

    return ("FAUX", initialiserTab2Dim(len(A), len(A[0]), PASCOLORE))  #retourne la matrice vide si c'est faux


def enumeration(A, sL, sC):

  (ok, G) = coloration(A, sL,sC)  #on applique l'algorithme de coloration au début
  if ok == "FAUX":
    return ("FAUX", initialiserTab2Dim(len(A), len(A[0]), PASCOLORE))  #retourne la matrice vide si c'est faux
  if ok == "VRAI":
    return ("VRAI", G)  #si coloration suffit pour trouver la solution, on la retourne

  #si coloration retourne ne sait pas
  G_copy = copy.deepcopy(G)
  (ok1, G1) = enumRec(G_copy, sL, sC, 0, BLANC)  #on applique l'algorithme avec la couleur blanc

  #si ok1 = VRAI alors G1 est la solution
  if ok1 == "VRAI":
    return ("VRAI", G1)

  (ok2, G2) = enumRec(G, sL, sC, 0, NOIR)  #on applique l'algorithme avec la couleur noir

  #si ok2 = VRAI alors G2 est la solution
  if ok2 == "VRAI":
    return ("VRAI", G2)

  #sinon on peut colorier cette case ni en blanc ni en noir -> pas de solution au puzzle
  return ("FAUX", initialiserTab2Dim(len(A), len(A[0]), PASCOLORE))


#algorithme de resolution complete (lecture du fichier .txt -> appliquer l'algo d'enumeration -> visualiser la grille coloriee)
def resolutionComplete(fichier):
  G, sL, sC = fichierToGrille(fichier)
  (ok, G1) = enumeration(G, sL, sC)
  print(ok)
  AfficherMatriceCouleur(G1)

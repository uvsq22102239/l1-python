carre_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 3, 13]]
print(carre_mag[0])
print(carre_mag[1])
print(carre_mag[2])
print(carre_mag[3])
print(carre_mag[0][1]) #14

carre_pas_mag = [i.copy() for i in carre_mag]
carre_pas_mag [3][2] = 7
print("Carre M", carre_mag)
print("Carre P", carre_pas_mag)

def afficheCarre(carre):
    """ Affiche la liste à 2 dimensions carre comme un carré"""
    for ligne in carre:
        for case in ligne:
            print(case, end="\t")
        print()

afficheCarre(carre_mag)
afficheCarre(carre_pas_mag)

def testLignesEgales(carre):
    """ Renvoie la somme des éléments d'une ligne de la liste 2D carre si toutes les lignes ont la même somme, et -1 sinon """
    cste = 0
    for ligne in carre:
        somme_ligne = 0
        for case in ligne:
            somme_ligne += case

        if carre.index(ligne) != 0 and somme_ligne != cste :
            return -1
        elif carre.index(ligne) == 0:
            cste = somme_ligne
    return cste
            
print("Carre M: cste ligne", testLignesEgales(carre_mag))
print("Carre P: cste ligne", testLignesEgales(carre_pas_mag))

def testColonnesEgales(carre):
    """ Renvoie la somme des éléments d'une colonne de la liste 2D carre si toutes les colonnes ont la même somme, et -1 sinon """
    sommes = [i for i in carre[0]] #façon compactée de déclarer une liste

    for ligne in carre[1:]:
        for j in range(len(ligne)):
            sommes[j] += ligne[j]

    cste = sommes[0]
    for s in sommes[1:]:
        if s != cste :
            return -1

    return cste

print("Carre M: cste colonne",testColonnesEgales(carre_mag))
print("Carre P: cste colonne",testColonnesEgales(carre_pas_mag))

def testDiagonalesEgales(carre):
    """ Renvoie la somme des éléments d'une diagonale de la liste 2D carre si les 2 diagonales ont la même somme, et -1 sinon """
    taille = len(carre[0])

    cste = 0
    for i in range(taille):
        cste += carre[i][i]
        #somme += carre[i][taille-i]
    
    somme = 0
    for i in range(taille, 0, -1):
        somme += carre[i-1][i-1]

    if somme != cste:
        return -1
   
    return cste

print("Carre M: cste diagonale",testDiagonalesEgales(carre_mag))
print("Carre P: cste diagonale",testDiagonalesEgales(carre_pas_mag))

def estCarreMagique(carre):
    """ Renvoie True si c'est un carre magique et False sinon"""
    A = 0
    if (testLignesEgales(carre) != -1) and (testColonnesEgales(carre) != -1) and (testDiagonalesEgales(carre) != -1):
        A = True
    else:
        A = False
    return A


print(estCarreMagique(carre_mag))
print(estCarreMagique(carre_pas_mag))

def estNormal(carre):
    """ Retourne True si contient toutes les valeurs de 1 à n^2 où n est la taille 
        du carré, et False sinon """
    all = []
    for ligne in carre:
        for elem in ligne:
            if all.count(elem) > 0:
                return False
            all.append(elem)
    
    taille = len(carre)
    if all[0] != pow(taille, 2):
        return False

    return True

print(estNormal(carre_mag))
print(estNormal(carre_pas_mag))
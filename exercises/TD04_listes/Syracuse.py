def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    suite = [n]

    value = n
    while value != 1:
        if value %2 == 0 :
            value = int(value/2)
        else:
            value = value * 3 + 1
        suite.append(value)

    return suite

def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 2 à n_max """
    
    for n in range (2, n_max):
        liste = syracuse(n)
    return True

 
print(f'Syracuse : {syracuse(3)}')
#print(f'Conjecture : {testeConjecture(10000)}')

def tempsVol(n):
    """ Retourne le temps de vol de n """
    return len(syracuse(n))-1

print("Le temps de vol de", 3, "est", tempsVol(3))

def tempsVolListe(n_max):
    """ Retourne la liste de tous les temps de vol de 1 à n_max """
    liste = []
    for n in range(1, n_max):
        liste.append(tempsVol(n))
    return liste

print(tempsVolListe(100))

def TempsVolMax(n_max):
    max = (0, 0) #(n, tempsVol)
    for n in range (1, n_max):
        temps = tempsVol(n)
        if max[1] < temps :
            max = (n, temps)
    return max

def Altitude(n):
    altitudes = syracuse(n)
    altitudes.remove(n)
    altitudes.sort(reverse=True)
    return altitudes[0]

def AltitudeMax(n_max):
    max = (0, 0) #(n, altitude)
    for n in range(2, n_max): # 2 ici pour pas avoir une erreur et tourner en rond, si  1 liste vide en paramètre
        altitude = Altitude(n)
        if max[1] < altitude:
            max = (n, altitude)
    return max
temps = (3, 23, 1, 34)
def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    return temps[3] + 60*temps[2] + 60*60*temps[1] + 60*60*24*temps[0]
print(type(temps))
print(tempsEnSeconde(temps))


def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    temps_jours = seconde // (24 * 3600)
    seconde = seconde % (24 * 3600)

    temps_heures = seconde//3600
    seconde = seconde % 3600

    temps_minutes = seconde // 60
    temps_secondes = seconde % 60

    return (int(temps_jours), int(temps_heures), int(temps_minutes), int(temps_secondes))
temps = secondeEnTemps(100000)
print(temps[0], "jours", temps[1], "heures", temps[2], "minutes", temps[3], "secondes")

def afficheTemps(temps):
    str_temps = ""
    if temps[1] > 0 :
        str_temps += f'{temps[0]} jours'
    elif temps[0] > 0 :
        str_temps += f'{temps[0]} jour'
    if temps[0] > 0 and (temps[1] > 0 or temps[2] > 0 or temps[3] > 0):
        str_temps += ", "
    if temps[1] > 1 :
        str_temps += f'{temps[1]} heures'
    elif temps[1] > 0 :
        str_temps += f'{temps[1]} heure'
    if temps[1] > 0 and (temps[2] > 0 or temps[3] > 0):
        str_temps += ", "
    if temps[2] > 1 :
        str_temps += f'{temps[2]} minutes'
    elif temps[2] > 0 :
        str_temps += f'{temps[2]} minute'
    if temps[2] > 0 and temps[3] > 0:
        str_temps += ", "
    if temps[3] > 1 :
        str_temps += f'{temps[3]} seconde'
    elif temps[3] > 0 :
        str_temps += f'{temps[3]} seconde'
    return print(str_temps)

def demandeTemps():
    jour = 0
    jour = int(input("Quel est le nombre de jour de votre valeur ?"))
    while jour > 365 or jour < 0:
        jour = int(input("Il faut que le nombre de jour soit cohérent."))
    heure = 0
    heure = int(input("Quel est le nombre d'heure de votre temps?"))
    while heure > 24 or jour < 0:
        heure = int(input("Il faut que le nombre d'heure soit cohérent."))
    minute = 0
    minute = int(input("Quel est le nombre de minute de votre valeur ?"))
    while minute > 60 or minute < 0:
        minute = int(input("Il faut que le nombre de minute soit cohérent."))
    seconde = 0
    seconde = int(input("Quel est votre nombre de seconde dans votre temps ?"))
    while seconde > 60 or seconde < 0:
        seconde = int(input("Il faut que le nombre de seconde soit cohérent."))
    return (jour, heure, minute, seconde)
# afficheTemps(demandeTemps())

def sommeTemps(temps1, temps2):
    seconde_t1 = tempsEnSeconde(temps1)
    seconde_t2 = tempsEnSeconde(temps2)

    return secondeEnTemps(seconde_t1+seconde_t2)

def proportionTemps(temps, proportion):
    seconde_t = tempsEnSeconde(temps)

    return secondeEnTemps(seconde_t*proportion)

def tempsEnDate(temps):
    jour, heure, minute, seconde = temps
    annee = 1970 + jour // 365
    jour %= 365
    return (annee, jour, heure, minute, seconde)


def afficheDate(date=-1):
    annee, jour, heure, minute, seconde = date
    print("Année", annee, end = ", ")
    afficheTemps((jour, heure, minute, seconde))


temps = secondeEnTemps(1000000000)
afficheTemps(temps)
afficheDate(tempsEnDate(temps))
afficheDate()

"""def nombreBisextile(jour):
    annee = 1970
    while(jour >= 0):
        if(annee % 4 == 0 and (annee %100 != 0 or annee % 400 == 0)):
            print("Année", annee, "bisextile")
            jour -= 366
        else:
            jour -= 365
        annee += 1
 print(nombreBisextile(200000))"""

def nombreBisextile(jour):
    nb_bisextile=0

    annee = 1970
    while(jour >= 0):
        if (annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0)):
            nb_bisextile += 1
            jour -= 366
        else:
            jour -= 3-5
        annee += 1
    return nb_bisextile 

def tempsEnDateBisextile(temps):
    jour, heure, minute, seconde = temps
    
    jour -= nombreBisextile(jour)
    annee = 1970 + jour // 365
    jour %= 365

    return (annee, jour, heure, minute, seconde)


def afficheDateComplete(date=-1):
    if date == -1:
        date = tempsEnDateComplete(secondeEnTemps(int(time.time()))) #fct optionnel qui prend en charge les mois
    annee, mois, jour, heure, minute, seconde = date #faudrait import time etc
    print("Année", annee, end=", ")
    print("mois", mois, end=", ")
    afficheTemps((jour, heure, minute, seconde))

def verifie(liste_temps):
    temps_month=0
    for month in liste_temps:
        temps_month=0
        for semaine in month:
            if semaine > 48 :
                print(f'L\'employé a trop de temps de travail en semaine')
                break
            temps_month += semaine
        if temps_month > 140 :
            print(f'L\'employé a trop de travail dans un même mois')

liste_temps = [[1,2,39,34],[0,1,9,4],[0,29,39,51],[0,31,13,46]]
verifie(liste_temps)

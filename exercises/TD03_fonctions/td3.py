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

def sommeTemps(temps1, temps2):
    seconde_t1 = tempsEnSeconde(temps1)
    seconde_t2 = tempsEnSeconde(temps2)

    return secondeEnTemps(seconde_t1+seconde_t2)

def proportionTemps(temps, proportion):
    seconde_t = tempsEnSeconde(temps)

    return secondeEnTemps(seconde_t*proportion)
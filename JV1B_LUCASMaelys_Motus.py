from colorama import init
init()

liste = ("Piquer","Manger","Ecoute","Retour","Cadrer","Yaourt")

#Je définis les mots que le jeu peut proposer
def mots():
    mot = input("Choissisez un mot à faire deviner :")
    motcaché=" "

#Je le cache en remplaçant les lettres par des points
    for i in range(len(mot)):
        motcaché=motcaché+"."
    print(motcaché)

#Le joueur propose alors une combinaison de lettre pour tenter de trouver le mot mystère
    lettre =input("Choissez une lettre (en prenant en compte les majuscules):")
    for i in range(len(mot)):
        if lettre == mot[i]:
            motcaché=motcaché+lettre
            from colorama import Fore, Back, Style
            print(Fore.BLUE)
            print(Style.BRIGHT)
            print(lettre)
            print(Style.RESET_ALL)
            
        
#Le système ne fonctionne pas et je pleure

        else: 
            lettre != mot[i]
            motcaché=motcaché+lettre
        from colorama import Fore, Back, Style
        print(Fore.RED)
        print(Style.BRIGHT)
        print("_")
        print(Style.RESET_ALL)

#Après je ne sais pas/plus comment sauvegarder une donnée ou faire une boucle pour continuer le jeu.
    lettre =input("Choissez à nouveau une lettre:")
    for i in range(len(mot)):
        if lettre == mot[i]:
            motcaché=motcaché+lettre
            from colorama import Fore, Back, Style
            print(Fore.BLUE)
            print(Style.BRIGHT)
            print(lettre)
            print(Style.RESET_ALL)

        else: 
            lettre != mot[i]
            motcaché=motcaché+lettre
        from colorama import Fore, Back, Style
        print(Fore.RED)
        print(Style.BRIGHT)
        print("_")
        print(Style.RESET_ALL)


mots()
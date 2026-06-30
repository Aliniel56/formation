#Exercice 6
"""Définition des fonctions"""
#def menu_capital():
#    print("Bonjour et bienvenu dans ce recueil de Capitale du monde !")
#    print("Voici les options qui s'offrent à toi !")
#    print("1. Consulter la liste des pays disponible")
#    print("2. Ajouter un nouveau pays et sa capitale")
#    print("3. Modifier un couple pays / capitale")
#    print("4. Supprimer un pays et sa capitale")
#    print("5. Quitter")
#def print_country():
#    for keys in capitals.keys():
#        print(keys)
#def add_country():
#    new_country_name = input("Quel pays souhaites-tu ajouter ? : ")
#    new_country_capital = input("Quelle est sa capitale ?")
#    capitals[new_country_name.lower().strip()] = new_country_capital.lower().strip()
#    print("Recueil mis à jour avec succès !")
#
#"""Dictionnaire"""
#capitals = {
#    "france" : "paris",
#    "angleterre" : "londres",
#    "espagne" : "madrid",
#    "italie" : "rome",
#    "allemagne" : "berlin"
#}
#
#"""Menu"""
#while True:
#    menu_capital()
#    user_choice = int(input("Quel est ton choix ? : "))
#    if user_choice == 5:
#        break
#    elif user_choice == 1:
#        print_country()
#        while True:
#            country = input("Quel pays souhaites-tu consulter ? ('retour' pour revenir au menu précédent) : ")
#            country = country.lower().strip()
#            if country == "retour":
#                print("Très bien, retour au menu précédent")
#                break
#            elif country in capitals:
#                print(f"La capital de {country} est : {capitals[country]}")
#            else:
#                print("Ce pays n'est pas dans la liste.")
#    elif user_choice == 2:
#        add_country()
#    elif user_choice == 3:
#        while True:
#            modify_country_choice = input("De quel pays souhaites tu modifier la capitale ? : ")
#            if modify_country_choice not in capitals.keys():
#                print("Ce pays n'est pas dans la liste !")
#            else:
#                modify_country = input(f"Quel est la nouvelle capitale que tu souhaites entrer pour le pays {modify_country_choice} : ")
#                capitals[modify_country_choice] = modify_country
#                print(f"La capitale de {modify_country_choice} à été modifié !")
#                break
#    elif user_choice == 4:
#        while True:
#            del_country = input("Quel pays souhaites-tu supprimer ? : ")
#            if del_country not in capitals.keys():
#                print("Ce pays n'est pas dans la liste !")
#            else:
#                del capitals[del_country]
#                print(f"Le pays {del_country} a été supprimé avec succès ! ")
#                break
#    else:
#        print("Choix invalide")

#Exercice 7
ages = {
    "Alice": 30,
    "Bob": 25,
    "Charlie": 35,
    "Diana": 28
}
oldest_name = ""
oldest_age = 0
for name, age in ages.items():
    if age > oldest_age:
        oldest_age = age
        oldest_name = name

print(f"La personne la plus âgée est {oldest_name} et elle a {oldest_age} ans.")


#Exercice 8
fr_en = {
    "chat": "cat",
    "chien": "dog",
    "oiseau": "bird"
}
en_fr = {

}
for fr, en in fr_en.items():
    en_fr[en] = fr
print(en_fr)

#Exercice 9
votes_list = ["oui", "non", "oui", "blanc", "oui", "non"]
votes_count = {}
for vote in votes_list:
    if vote in votes_count:
        votes_count[vote] += 1
    else:
        votes_count[vote] = 1
print(votes_count)

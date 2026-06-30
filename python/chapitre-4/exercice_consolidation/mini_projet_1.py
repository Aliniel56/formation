#Liste de courses

"""Definition des fonctions"""
def menu_grocery(): #Afficher le menu
    print("Bienvenu dans ce gestionnaire de liste de courses, voici les options :")
    print("1. Ajouter un article (ou augmenter la quantité si déjà existant)")
    print("2. Retirer un article (ou diminuer la quantité d'un article)")
    print("3. Afficher la liste de course")
    print("4. Quitter")

def add_article(): #Ajouter un article ou augmenter sa valeur
    new_article_name = input("Quel article souhaites tu ajouter ? : ").lower().strip()
    new_article_quantity = int(input(f"Quel quantité de {new_article_name} souhaites tu ajouter ? : "))
    if new_article_name in grocery.keys():
        grocery[new_article_name] += new_article_quantity
    else :
        grocery[new_article_name] = new_article_quantity

def remove_article():
    remove_article_name = input("De quel article retirer ? : ").lower().strip()
    if remove_article_name not in grocery:
        print("Cet article n'est pas dans la liste.")
        return
    
    remove_article_quantity = int(input(f"Combien de {remove_article_name} retirer ? : "))
    grocery[remove_article_name] -= remove_article_quantity
    if grocery[remove_article_name] <= 0:
        del grocery[remove_article_name]
        print(f"{remove_article_name} a été retiré de la liste.")
    else:
        print(f"Il reste {grocery[remove_article_name]} {remove_article_name}.")

"""Dictionnaire"""
grocery = {"pommes" : 1, "poire" : 1}

"""Programme"""
while True:
    menu_grocery()
    user_choice = int(input("Quelle options souhaites-tu utiliser ? : "))
    if user_choice == 4:
        break
    elif user_choice == 1:
        add_article()
    elif user_choice == 2:
        remove_article()
    elif user_choice == 3:
        print(grocery)
    else:
        print("Choix invalide")

#Exercice 8

"""FONCTION A DÉFINIR"""
def menu():
    print("--- MENU DU CARNET D'ADRESSE ---")
    print("1. Ajouter un contact")
    print("2. Chercher un contact")
    print("3. Afficher tous les contacts")
    print("4. Supprimer un contact")
    print("5. Quitter")
def add_contact():
    new_contact_name = input("Quel contact veux tu ajouter ? : ")
    new_contact_number = input("Quel est son numéro ? : ")
    contact[new_contact_name.lower().strip()] = new_contact_number.strip()
    print("Liste des contacts mise à jour avec succès !")
def show_contact():
    print("Liste des contacts du carnet d'adresse :")
    print(contact)

"""DICTIONNAIRE"""
contact = {
    "jean" : "0102030405",
    "bernard" : "0203040506"
}

"""MENU"""
while True:
    menu()
    user_choice = int(input("Quel est ton choix ? : "))
    if user_choice == 5:
        break
    elif user_choice == 1:
        add_contact()
        while True:
            user_choice_next = input("Veux-tu afficher la liste des contacts mise à jour ? (oui / non) : ")
            if user_choice_next.lower().strip() == "non":
                break
            elif user_choice_next.lower().strip() == "oui":
                show_contact()
                break
            else:
                print("Choix invalide")
    elif user_choice == 2:
        while True:
            is_contact_name = input("Quel contact souhaites-tu chercher ? (exit pour sortir) : ")            
            if is_contact_name.lower().strip() in contact:
                while True:
                    is_contact_show = input("Ce contact existe ! Souhaites-tu l'afficher ? (oui / non) : ")
                    if is_contact_show.lower().strip() == "oui":
                        print(f" Nom : {is_contact_name.lower().strip()}; Numéro : {contact[is_contact_name.lower().strip()]}")
                        break
                    elif is_contact_show.lower().strip() == "non":
                        print("Très bien on retourne au menu précédent")
                        break
                    else:
                        print("Choix invalide")
                break
            elif is_contact_name.lower().strip() == "exit":
                break
            else:
                print(f"Aucun contact nommé {is_contact_name}")
    elif user_choice == 3:
        show_contact()
    elif user_choice == 4:
        while True:
            contact_del = input("Quel contact souhaites-tu supprimer ? (exit pour sortir) : ")
            if contact_del.lower().strip() == "exit":
                break
            elif contact_del.lower().strip() in contact:
                del contact[contact_del.lower().strip()]
                print("Contact supprimé avec succès !")
                while True:
                    user_choice_next = input("Veux-tu afficher la liste des contacts mise à jour ? (oui / non) : ")
                    if user_choice_next.lower().strip() == "non":
                        break
                    elif user_choice_next.lower().strip() == "oui":
                        show_contact()
                        break
                    else:
                        print("Choix invalide")
                break
            else:
                print("Choix invalide")
    else:
        print("Choix invalide")

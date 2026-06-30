#Mini programme 2 - Mini jeu du menu
import datetime
today = datetime.date.today()

while True:    
    print("--- MENU ---")
    print("1. Dire bonjour")
    print("2. Afficher la date du jour")
    print("3. Compter jusqu'à 5")
    print("4. Quitter")
    user_choice = int(input("Quel est ton choix ? : "))
    if user_choice == 4:
        print("Bien joué ! A bientôt !")
        break
    elif user_choice == 1:
        print("Bonjour")
    elif user_choice == 2:
        print(today.strftime("Aujourd'hui nous sommes le %d/%m/%Y"))
    elif user_choice == 3:
        for i in range(1,6):
            print(i)
    else:
        print("Choix invalide")


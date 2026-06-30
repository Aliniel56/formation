#Exercice 7

import random

def get_valid_guess():
    """Demande un essai à l'utilisateur et le renvoie."""
    guess = int(input("Ton essai : "))
    while guess < 1 or guess > 100:
        print("Le nombre doit être compris entre 1 et 100 !")
        guess = int(input("Ton essai : "))
    return guess

secret = random.randint(1, 100)
attempts = 0
found = False

print("Je pense à un nombre entre 1 et 100. A toi de le deviner, mais attention, tu n'as le droit qu'à 7 essaies. Bonne chance !")

while not found and attempts < 7:
    guess = get_valid_guess()
    attempts += 1
    if guess == secret:
        found = True
        print(f"Bravo ! Tu as trouvé en {attempts} essais.")
    elif guess < secret:
        print("C'est plus grand")
    else:
        print("C'est plus petit")

if not found:
    print(f"Dommage, tu auras plus de chance la prochaine fois ! Le nombre était : {secret}.")

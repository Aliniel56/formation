# Jeu : deviner le nombre secret !

secret = 7
attempts = 0
found = False

print("Je pense à un nombre entre 1 et 10. A toi de le deviner !")

while not found :
    guess = int(input("Ton essai : "))
    attempts += 1

    if guess == secret:
        found = True
        print(f"Bravo ! Tu as trouvé en {attempts} essais.")
    elif guess < secret:
        print("C'est plus grand")
    else:
        print("C'est plus petit")
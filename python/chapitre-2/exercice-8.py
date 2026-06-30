#Exercice 8
import random
secret = random.randint(1, 100)
attempts = 0
found = False

print("Je pense à un nombre entre 1 et 100. A toi de le deviner, mais attention, tu n'as le droit qu'à 7 essaies. Bonne chance !")

while not found and attempts < 7:
    guess = int(input("Ton essai : "))
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

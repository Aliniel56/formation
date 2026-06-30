#Exercice 2
note = int(input("Quel note /20 as tu eu à l'exercice ? "))
if note >= 16:
    print("Mention Très Bien !")
elif note >= 14:
    print("Mention Bien !")
elif note >= 12:
    print("Mention Assez Bien !")
elif note >= 10:
    print("Reçu sans mention !")
else:
    print("Recalé !")

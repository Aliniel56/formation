#Exercice 4
notes_list = []
how_many_notes = int(input("Combien de notes veux tu rentrer ? : "))
for i in range(how_many_notes):
    notes = float(input("Quelles sont les notes à entrer pour la moyenne ? : "))
    notes_list.append(notes)
average = sum(notes_list) / len(notes_list)
print(f"La moyenne des notes est de {average} points")
print(f"La meilleure note est : {max(notes_list)}")
print(f"La moins bonne note est : {min(notes_list)}")
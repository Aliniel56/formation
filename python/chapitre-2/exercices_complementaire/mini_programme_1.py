how_many_notes = int(input("Combien de notes veux tu rentrer ? : "))

first_note = float(input("Qu'elle est la note à rentrer ? : "))

total_notes = first_note
highest = first_note
lowest = first_note

for i in range(how_many_notes - 1):
    notes = float(input("Qu'elle est la note à rentrer ? : "))
    total_notes += notes
    if notes > highest:
        highest = notes
    if notes < lowest:
        lowest = notes
moyenne = total_notes / how_many_notes
print(f"La moyenne est de : {moyenne} points !")
print(f"Meilleure note : {highest}")
print(f"Moins bonne note : {lowest}")


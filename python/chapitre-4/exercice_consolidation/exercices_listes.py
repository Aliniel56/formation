##Exercices Listes
#Exercices 1
notes = [12, 15, 9, 18, 11, 7, 14]

print(f"La moyenne est de : {(sum(notes) / len(notes)):.2f}.")
print(f"La note maximale est de : {max(notes)}.")
print(f"La note minimale est de : {min(notes)}.")
print(f"L'écart entre la note maximale et la note minimale est de {(max(notes) - (min(notes)))} points.")

#Exercice 2
numbers = [1, 2, 3, 4, 5]
print(numbers[::-1])
numbers.reverse()
print(numbers)

#Exercice 3
numbers_2 = [4, 7, 10, 15, 22, 33, 8]
numbers_2_new = []

for number in numbers_2:
    if number > 10:
        numbers_2_new.append(number)

print(numbers_2_new)

#Exercice 4
fruits = ["pomme", "banane", "kiwi", "pomme", "fraise", "pomme"]
fruits_pomme = []
for fruit in fruits:
    if fruit.lower().strip() == "pomme":
        fruits_pomme.append(fruit)
print(f"Il y a {len(fruits_pomme)} pommes dans la liste !")

#Exercice 5
list_a = [3, 1, 4]
list_b = [5, 2, 6]
list_total = list_a + list_b
list_total.sort()
print(list_total)
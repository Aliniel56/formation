fruits = ["pomme", "banane", "cerise"]

for fruit in fruits:
    print(f"J'ai les {fruit}s")


#Calcul de moyenne avec liste
notes_list = []
how_many_notes = int(input("Combien de notes veux tu rentrer ? : "))
for i in range(how_many_notes):
    notes = float(input("Quelles sont les notes à entrer pour la moyenne ? : "))
    notes_list.append(notes)
average = sum(notes_list) / len(notes_list)
print(f"La moyenne des notes est de {average} points")
print(f"La meilleure note est : {max(notes_list)}")
print(f"La moins bonne note est : {min(notes_list)}")

#Calculatrice avec liste et dictionnaire
def get_number():
    a = int(input("Choisis un nombre a : "))
    b = int(input("Choisis un nombre b : "))
    return a, b
def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if b == 0:
        return "Impossible de diviser par 0"
    return a / b
operation_list = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}
while True:
    print("--- Calculatrice ---")
    operation = input("Choisis ton opération (+, -, *, /). Tape 'exit' pour quitter : ")
    if operation.lower().strip() == "exit":
        break
    a, b = get_number()
    if operation in operation_list:
        chosen_function = operation_list[operation]
        result = chosen_function(a, b)
        print(f"Résultat = {result}")
    else:
        print("Opération inconnu")

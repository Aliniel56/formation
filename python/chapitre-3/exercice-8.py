#Exercice 8
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
while True:
    print("--- Calculatrice ---")
    operation = input("Choisis ton opération (+, -, *, /). Tape 'exit' pour quitter : ")
    if operation == "exit":
        break
    a, b = get_number()
    if operation == "+":
        result = add(a,b)
    elif operation == "-":
        result = subtract(a,b)
    elif operation == "*":
        result = multiply(a,b)
    elif operation == "/":
        result = divide(a,b)
    else:
        result = "Opération inconnue"
    print(f"Résultat : {result}")




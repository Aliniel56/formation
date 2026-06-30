#Exercice A1
print("Exercice A1")
for a in range(1,21):
    print(f"Nombre {a}")

#Exercice A2
print("Exercice A2")
for b in range(20,0,-1):
    print(f"Numéro {b}")

#Exercice A3
print("Exercice A3")
for c in range(0,31,3):
    print(f"Numéro {c}")

#Exercice A4
print("Exercice A4")
total = 0
for d in range(1,51):
    if d % 2 == 0:
        total += d
print(total)

#Exercice A5
print("Exercice A5")
spell_word = input("Donne moi un mot de ton choix : ")
for letter in spell_word:
    print(letter)

#Exercice A6
print("Exercice A6")
e = int(input("Donne moi un chiffre : "))
for n in range(1, e+1):
    print(f"Tour {n}")

#Exercice A7
print("Exercice A7")
f = int(input("Donne moi un chiffre positif : "))
while f < 0:
    f = int(input("Donne moi un chiffre positif : "))
if f > 0:
    print("Merci !")

#Exercice A8
print("Exercice A8")
start = 1
while start < 1000:
    start += start


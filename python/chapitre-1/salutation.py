prénom = input("Quel est ton prénom ?")
age = int(input("Quel est ton age ?"))
année_courante=2026
année_naissance = année_courante - age
est_majeur = age >= 18

print(f"Bonjour, tu t'appelle {prénom}, tu as {age} ans, ce qui veut dire que tu es né en {année_naissance} tu es donc majeur : {est_majeur}")
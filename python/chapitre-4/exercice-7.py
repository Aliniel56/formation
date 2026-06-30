#Exercice 7
input_word = []
for i in range(5):
    word = input("Donne moi un mot de ton choix (tu peux me donner le même plusieurs fois) : ")
    input_word.append(word.lower().strip())
unique_input_word = set(input_word)
print(f"Tu m'as donné {len(unique_input_word)} mots uniques")
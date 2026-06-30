#Exercice 9
def count_vowels(text):
    vowels = 0
    for letter in text:
        if letter.lower() in "aeiou":
            vowels += 1
    return vowels

word = input("Donne moi un mot pour compter les voyelles : ")
result = count_vowels(word)
print(f"Il y a {result} voyelles dans le mot '{word}' !")

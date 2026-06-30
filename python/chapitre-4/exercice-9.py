#Exercice 9
def count_words(text):
    counts = {}
    words = text.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

result = count_words("le chat le chien le")
print(result)
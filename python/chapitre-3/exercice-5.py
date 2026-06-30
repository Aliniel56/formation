#Exercice 5
def is_even(number):
    if number % 2 ==0:
        return True
    else:
        return False
    
print(is_even(5))

def is_even_2(number):
    return number % 2 == 0

print(is_even_2(5))

#Les deux renvoie un résultat identique, mais je ne sais pas pourquoi, sûrement une histoire sur le fais qu'un résultat ne peut être que True ou False, mais je n'arriverai pas à l'expliquer clairement.
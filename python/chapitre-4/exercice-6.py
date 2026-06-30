#Exercice 6
prices = {
    "produit 1" : 10,
    "produit 2" : 20,
    "produit 3" : 30,
    "produit 4" : 40
}

for key, value in prices.items():
    print(f"Le {key} coûte {value} euros.")

total_price = sum(prices.values())

print(f"Le montant total de tout les produits est de {total_price} euros.")
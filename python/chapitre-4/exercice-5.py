#Exercice 5
game_character = {
    "name": "Alfred",
    "level": 999,
    "health": 5000,
    "class" : "Guerrier"
}

print(f"Le nom de ton personnage est {game_character["name"]}, c'est un {game_character["class"]} de niveau {game_character["level"]} et il possède actuellement {game_character['health']} points de santé.")

game_character["level"] = 1000
game_character["health"] = 5500

print(f"Bien joué ! Tu montes d'un niveau !")
print(f"Statistiques actuelles : ")
print(f"Niveau : {game_character['level']}")
print(f"Santé : {game_character['health']}")
import random

def play_game():
    print("Bienvenue au jeu pierre-feuille-ciseaux !")
    print("Le premier joueur à remporter 3 manches gagne la partie.\n")

    player_score = 0
    computer_score = 0

    while player_score < 3 and computer_score < 3:
        print("Score : Joueur", player_score, "- Ordinateur", computer_score)

        player_choice = input("Pierre, feuille ou ciseaux ? ").lower()
        while player_choice not in ["pierre", "feuille", "ciseaux"]:
            player_choice = input("Veuillez choisir entre pierre, feuille ou ciseaux : ").lower()

        computer_choice = random.choice(["pierre", "feuille", "ciseaux"])
        print("L'ordinateur a choisi", computer_choice + ".")

        if player_choice == computer_choice:
            print("Egalité !\n")
        elif (player_choice == "pierre" and computer_choice == "ciseaux") \
            or (player_choice == "feuille" and computer_choice == "pierre") \
            or (player_choice == "ciseaux" and computer_choice == "feuille"):
            player_score += 1
            print("Le joueur remporte cette manche !\n")
        else:
            computer_score += 1
            print("L'ordinateur remporte cette manche !\n")

    if player_score > computer_score:
        print("Bravo, vous avez gagné la partie !")
    else:
        print("Dommage, l'ordinateur a gagné la partie.")

play_game()

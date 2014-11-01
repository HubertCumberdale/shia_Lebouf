import dark_forest
from game_functions import dead
from game_functions import print_slow


def start():
    print_slow("Do you want to play a word game about Shia Lebouf?\n\n")

    choice = raw_input("---> ")

    if choice.lower() in ["yes", "y", "sure"]:
        dark_forest.dark_forest()
    else:
        dead("Fine! I didn't want to play with you anyway!")

start()


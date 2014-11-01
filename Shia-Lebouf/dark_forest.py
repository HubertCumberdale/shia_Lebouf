from sys import exit
import time
import game_functions
from game_functions import print_slow
import Lindsay_Lohan_House


def dark_forest():
    print_slow("You decide to go on a long walk through nature to clear your head of the horrible divorce you just "
               "had to endure.\n\n"
               "You ponder how your life has come to this. Your wife has all of your money - and dignity. \n\n"
               "You find your thoughts interrupted by a rustling sound about 30 feet behind you. You turn "
               "around to see what it is.\n\n"
               "'Mother of God!' you scream. Its Shia Lebouf! He begins running after you!\n\n"
               "****What do you do? Do you choose FIGHT or FLIGHT?****\n")


    choice = raw_input("---> ")

    if choice.lower() in ["fight", "battle", "war", "f"]:
        print_slow("Shia Lebouf is in rage mode you fool! Why would you choose to fight with those weak little arms!\n"
                   "\nYou stupidly charge him thinking you have a chance of winning. Shia sees you coming!")
        time.sleep(5)
        game_functions.dead("\n\nYou obviously have lost and died. Try again and don't fight Shia in rage mode!")

    elif choice.lower() in ["flight", "run", "run!", "r"]:
        print_slow("\n\nYou take off running as fast as you possibly can. You knew that "
                   "flip flops were a bad choice of footwear.\n\nRunning for what seems like an eternity, you see a "
                   "small house hidden in the woods.\n\nIt is getting dark and you have no choice but to try to take "
                   "cover in the house.\n\n")
        Lindsay_Lohan_House.lindsays_house()

    else:
        print_slow("That wasn't an option you moron. Try again.")
        dark_forest()


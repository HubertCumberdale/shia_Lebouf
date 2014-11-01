from game_functions import dead
from game_functions import win_game
from game_functions import print_slow
from game_functions import way_slow_print
import time


def lindsays_house():
    time.sleep(3)
    print_slow("\n\nThe house is eerily quiet as you enter. Your footsteps sound like dying rats as you walk on the"
               " floorboards.\n\n")
    time.sleep(2)
    way_slow_print("C R E A K...\n\n\n\n")
    time.sleep(2)
    way_slow_print("CRREEAAAK\n\n")
    time.sleep(2)
    print_slow("You look around and notice pictures are plastered everywhere of what looks like Lindsay Lohan.\n\n"
               "'Jesus H Christ...' you mumble under your breath. 'I'm in Lindsay's den of drugs... What do I do?'\n\n")
    time.sleep(4)
    print_slow("You see a pantry that you would be able to fit into. Should you hide in the pantry or find a weapon?\n\n")

    choice = raw_input("----> ")

    if choice in ["hide", "hide in pantry", "pantry"]:
        drug_pantry()
    elif choice in ["weapon","find a weapon","find"]:
        kitchen()
    else:
        print_slow("Say wwwhat? Weapon or Hide?")
        lindsays_house()


def drug_pantry():
    print_slow("You enter the drug pantry, quickly closing the door behind you.\n\nYou are terrified but feel as if you"
               " have lost the Shia monster.\n\nYou press your ear to the pantry door, struggling to listen for Shia"
               " sounds over the beating of your own heart.\n\n From the corner of your eye you barely notice movement,"
               " a slow white powdery object.\n\nSuddenly Lindsay/'s face rushes towards yours!")
    dead("You feel her biting and eating your neck, and slowly lose consciousness. You know your time is now at an end.")

def kitchen():
    print "You wander down a long hallway for what feels like an eternity along the way you stumble on some liquor" \
          "as you do you hear a devilish shriek in the that pantry you though about hiding in. your panic mode kicks in" \
          "again and you make a break down the hallway where you finally find yourself in a huge kitchen with evidence" \
          "of drug use everywhere, your tempted to do one line of coke that's plainly laying on the table" \
          "..you know. to calm the nerve a bit... do you take drugs? or walk away?"

    choice = raw_input("> ")

    if choice == "take drugs":
        print "that was the best damn line of coke you ever had! After doing it you see a breadcrumb line of coke" \
              "heading out of the kitchen down another hallway that leads back to that drug pantry."\
              "you think to yourself 'there must be more in that pantry' and being brave on coke" \
              "you decide that brick of this stuff could go a long way in getting back some of that" \
              "money your wife stole in the divorce. so you make your way to the pantry"
        time.sleep(10)
        drug_pantry()
    elif choice == "walk away":
        print "your whits come back and you realize that drugs are never good, even when impending death of" \
              "Shia lebouf is upon you."
        print "you continue looking for a weapon when you spot a rack of knives, you quickly grab the largest one."
        print "then suddenly you hear that shriek again and in the doorway is a zombie like pale white woman. " \
              "terron strikes your heart as you instantly know who this is! he is yelling a screaming but you cant" \
              "understand anything she is saying. She lunges at you and with that you burry it deep in her chest" \
              "you panic, 'did I just fucking kill lohan???'"
        time.sleep(5)
        kill_lohans()
    else:
        print "i am pretty stupid program and only understand to possible string here. try again"
        kitchen()


def kill_lohans():
    print_slow("***You have vanquished Lindsay Lohans!!!!!***")
    time.sleep(5)
    print_slow("Covered in blood and feces, you have to now make a decision on what do to. Do you want to stay here and"
               " fortify the house against the impending arrival of Shia Lebouf, or flee back into the woods to try to "
               "find your car?")

    choice = raw_input ("> ")


    if choice.lower() in ["flee", "woods", "flee back into woods", "into the woods", "to the woods", "car",
                          "find my car", "find your car","find car"]:
        return_2_da_woods()
    elif choice in ["fortify", "fortify the house", "fortify house", "house"]:
        shianal_stand()
    else:
        print_slow("Say wwwhat? Should you fortify or hide?")
        kill_lohans()


def return_2_da_woods():

    print_slow("Pussy azz nigga runnin back 2 da woods")
    dead("Shia Lebouf pooped in your heart")



def shianal_stand():
    print "let's finish this cunt!"
    print "Shia bursts through the door! You can see a piece of intestine hanging from his jaw as he screams for you" \
          "to come out. You have only a split second to decide what to do"
    print "Do you roundhouse kick him to the face, or do you knife him in the head?"

    choice = raw_input("> ")

    if choice == "roundhouse":
        dead("You're not Chuck Norris! Shia blocks your kick with ease and poops in your heart")

    elif "knife" in choice:
        print "Shia Lebouf takes the knife to the head and falls dead to the ground, your heart remains unpooped in. "
        win_game()
    else:
        print "No nintendo amigo. try again"
        shianal_stand()









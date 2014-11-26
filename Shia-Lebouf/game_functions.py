from sys import exit
from sys import stdout
import time


def print_slow(string):
    punctuation = [".", "!", "?"]

    for letter in string:
        stdout.write(letter)
        stdout.flush()

        if letter in punctuation:
            time.sleep(.5)
        else:
            time.sleep(.035)
    print("")

def way_slow_print(string):

    punctuation = [".", "!", "?"]

    for letter in string:
        stdout.write(letter)
        stdout.flush()

        if letter in punctuation:
            time.sleep(.7)
        else:
            time.sleep(.05)
    print ("")

def dead(why):
    print_slow(why)
    exit(0)


def win_game():
    print "Against all odds you have killed Shia Lebouf!"
    exit(0)
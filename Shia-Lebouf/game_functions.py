from sys import exit
from sys import stdout
import time


def print_slow(string):
    for letter in string:
        stdout.write(letter)
        time.sleep(.035)

def way_slow_print(string):
    for letter in string:
        stdout.write(letter)
        time.sleep(.7)

def dead(why):
    print_slow(why)
    exit(0)


def win_game():
    print "Against all odds you have killed Shia Lebouf!"
    exit(0)
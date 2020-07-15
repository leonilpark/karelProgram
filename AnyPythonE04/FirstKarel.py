from karel.stanfordkarel import *

"""
File: FirstKarel.py
------------------------
When you finish writing code in this file, FirstKarel should 
solve the problem. 
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    move()
    pick_beeper()
    move()
    leftGo()
    turn_right()
    doubleMove()
    put_beeper()
    move()

def turn_right():
    for i in range(0,3):
        turn_left()

def doubleMove():
    for i in range(0,2):
        move();
def leftGo():
    turn_left();
    move();

def rightGo():
    turn_right();
    move();

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()

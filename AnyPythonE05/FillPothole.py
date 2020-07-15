from karel.stanfordkarel import *

"""
File: FillPothall.py
------------------------
Fills the pothole beneath Karel's current position by 
placing a beeper on that corner. For this function to work 
correctly, Karel must be facing east immediately above the 
pothole. When execution is complete, Karel will have 
returned to the same square and will again be facing east.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    go(1);
    fill_hole();
    go(3);


def check_wall():
    while ():
        if not front_is_clear():
            turn_left()
            go(1)
        else:
            go(1)
            break;


def fill_hole():
    turn_right();
    move();
    put_beeper();
    turn_reverse();
    move();
    turn_right();

def go(some):
    for i in range(0,some):
        move();

def turn_reverse():
    for i in range(0, 2):
        turn_left();


def turn_right():
    for i in range(0,3):
        turn_left();

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()

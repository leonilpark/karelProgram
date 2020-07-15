from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    findnews()

def findnews():
    move()
    turn_left()
    if(front_is_clear()):
        getsome()
        turn_reverse()
        turn_left()
        move()
        turn_right()
        move()
        turn_left()
        if (front_is_clear()):
            getsome()
        else:
            turn_reverse()
            turn_left()
            move()
            turn_right()
            move()
            turn_left()

            if (front_is_clear()):
                getsome()
            else:
                turn_reverse()
                turn_left()
                move()
                turn_right()
                move()
                turn_left()
                if (front_is_clear()):
                    getsome()
                    turn_reverse()
                    turn_left()
                    move()
                else:
                    turn_reverse()
                    turn_left()
                    move()
    else:
        turn_reverse()
        turn_left()
        move()
        turn_right()
        move()
        turn_left()
        if (front_is_clear()):
            getsome()
            turn_reverse()
            turn_left()
            move()
            turn_right()
            move()
            turn_left()

            if (front_is_clear()):
                getsome()
            else:
                turn_reverse()
                turn_left()
                move()
                turn_right()
                move()
                turn_left()
                if (front_is_clear()):
                    getsome()
                    turn_reverse()
                    turn_left()
                    move()
                else:
                    turn_reverse()
                    turn_left()
                    move()
        else:
            turn_reverse()
            turn_left()
            move()
            turn_right()
            move()
            turn_left()

            if (front_is_clear()):
                getsome()
                turn_reverse()
                turn_left()
                move()
                turn_right()
                move()
                turn_left()
                if (front_is_clear()):
                    getsome()
                    turn_reverse()
                    turn_left()
                    move()
                else:
                    turn_reverse()
                    turn_left()
                    move()
            else:
                turn_reverse()
                turn_left()
                move()
                turn_right()
                move()
                turn_left()
                if (front_is_clear()):
                    getsome()
                    turn_reverse()
                    turn_left()
                    move()
                else:
                    turn_reverse()
                    turn_left()
                    move()


def getsome():
    move()
    pick_beeper()
    turn_reverse()
    move()
    turn_reverse()
def turn_reverse():
    for i in range(0, 2):
        turn_left()


def turn_right():
    for i in range(0,3):
        turn_left()
# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()

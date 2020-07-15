from karel.stanfordkarel import *

"""
File: EndpointCounter.py
------------------------
In this problem, Karel is in the top left corner of a 
square world. Karel needs to make his way down to a staircase
at the bottom left corner, and from there, he needs to place 
the same number of beepers on each step as there are blank 
spaces above Karel. For example, in a 10x10 world, karel must 
place 9 beepers on the first step (due to 1 being blocked by
a wall), then 8 in the next, and so on, until Karel reaches 
the top of the staircase.  
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """

    a =gocheck()
    for i in range(0, a):
        put_beeper()
    reverse()
    move()
    turn_left()
    move()
    a-=1
    while(True):
        for i in range(0,a):
            put_beeper()

        right()

        if front_is_clear():
            move()
            turn_left()
            move()
        else :
            break;
        a -= 1
def reverse():
    for i in range(0,2):
        turn_left()


def gocheck():
    a=1
    while(front_is_clear()):
        move()
        a +=1
    return a


def rightsidecheck():
    turn_left()
    while(front_is_blocked()):
        if beepers_present():
            return 1
def right():
    for i in range(0,3):
        turn_left()


# There is no need to edit code beyond this point
if __name__ == "__main__":
    run_karel_program()

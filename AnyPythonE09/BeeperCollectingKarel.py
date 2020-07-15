from karel.stanfordkarel import *

"""
File: BeeperCollectingKarel.py
------------------------
The BeeperCollectingKarel class collects all the beepers
in a series of vertical towers and deposits them at the
eastmost corner on 1st row.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    a = 0
    for i in range(0,4):
        a += twolineget()
    turn_left()
    for i in range(0,a):
        put_beeper()
    turn_reverse()
    go(8)

def twolineget():
    a = 0
    a += leftlineget()
    a += rightlineget()
    return a

def leftlineget():
    a = 0
    turn_left()
    while (front_is_clear()and not beepers_present()):
        if beepers_present():
            pick_beeper()
            a += 1
        go()
    return a
def rightlineget():
    a = 0
    turn_right()
    while (front_is_clear()and not beepers_present()):
        if beepers_present():
            pick_beeper()
            a += 1
        go()
    return a

def invertBeeper():
    if beepers_present():
        pick_beeper()
    else:
        put_beeper()

def manyBeeper(some):
    for i in range(some):
        put_beeper()
def escape_ziczac():
    a = 0
    while ():
        if (not front_is_clear() and a != 4):
            turn_left()
            go(1)
            a += 1
        elif (front_is_clear()):
            go(1)
        elif(a == 4):
            break;

def fill_hole():
    turn_right()
    move()
    put_beeper()
    turn_reverse()
    move()
    turn_right()

def go(some):
    for i in range(0,some):
        move()

def turn_reverse():
    for i in range(0, 2):
        turn_left()


def turn_right():
    for i in range(0,3):
        turn_left()
# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()

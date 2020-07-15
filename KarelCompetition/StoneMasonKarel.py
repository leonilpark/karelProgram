from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem. You should make sure that 
your program works for all of the sample worlds supplied in the 
starter folder.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    while (True):
        a = checkline()

        returnline()
        if (a == 1):
            beepercr()
            returnline()

        turn_left()
        if(front_is_blocked()):
            break
        else:
            move()



def beepercr():
    turn_reverse()
    while(front_is_clear()):
        if(not beepers_present()):
            put_beeper()
        move()
    if front_is_blocked() and (not beepers_present()):
        put_beeper()



def returnline():
    turn_reverse()
    while(True):
        if(front_is_blocked()):
            break;
        move()


def checkline():
    turn_left()
    if(beepers_present()):
        return 1
        turn_right()
    else:
        while (front_is_clear()):
            move()
            if (beepers_present()):
                return 1
    return 0
def otherline():
    if front_is_blocked():
        return 2
    move()
    if (beepers_present()):
        return 1
    else:
        while (front_is_clear()):
            move()
            if (beepers_present()):
                return 1



def zic_right():
    turn_right()
    go(1)

def zic_left():
    turn_left()
    go(1)

def twolineget():
    a = 0
    a += leftlineget()
    a += rightlineget()
    return a

def leftlineget():
    a = 0
    turn_left()
    while (front_is_clear()):
        if not beepers_present():
            put_beeper()
        move()
    return a
def rightlineget():
    a = 0
    turn_right()
    while (front_is_clear()):
        if not beepers_present():
            put_beeper()
        move()
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

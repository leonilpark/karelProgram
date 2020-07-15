from karel.stanfordkarel import *
import pyautogui

"""
File: RunwayKarel.py
------------------------
The RunawayKarel class makes Karel run away to the wall.
The class asks a user which direction a Karel is running
away, i.e., either East, West, South, or North. Then, 
a Karel is moving to the wall with the direction.
Extra: After arriving at the edge, put beepers as many Karel moved.
For example, if Karel moved 2 corners, put 2 beepers.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """

    while(True):
        a = input("방향키는 wasd, 박스놓기는 p, 줍기는 o입니다. 끝내기는 q입니다. \n 입력 : ")
        if(front_is_clear()):
            if (a == "a"):
                goleft()
            elif (a == "s"):
                godown()
            elif (a == "w"):
                goup()
            elif (a == "d"):
                goright()
            elif (a == "p"):
                put_beeper()
            elif (a == "o"):
                pick_beeper()
            elif (a == "q"):
                exit()
        e


def goup():
    turn_left()
    move()
    turn_right()
def godown():
    turn_right()
    move()
    turn_right()
def goleft():
    turn_reverse()
    move()
    turn_reverse()
def goright():
    move()

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


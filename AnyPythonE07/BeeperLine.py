from karel.stanfordkarel import *

"""
File: BeeperLine.py
------------------------
Uses a while loop to place a line of beepers.
This program works for a world of any size.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    while(front_is_clear()):
        put_beeper()
        move()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program("7x7.w")

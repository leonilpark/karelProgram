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
    #pass
    collect_all_beepers()
    drop_all_beepers()
    return_home()

# Collects the beepers from every tower by moving along 1st
# row, calling collectOneTower at every corner.  The
# postcondition for this method is that Karel is in the
# easternmost corner of 1st row facing east.
def collect_all_beepers():
    while front_is_clear():
        collect_one_tower()
        move()
    collect_one_tower()

# Collects the beepers in a single tower. When collectOneTower
# is called, Karel must be on 1st row facing east.  The
# postcondition for collectOneTower is that Karel must again
# be facing east on that same corner.
def collect_one_tower():
    turn_left()
    collect_line_of_beepers()
    turn_around()
    move_to_wall()
    turn_left()

# Collects a consecutive line of beepers. The end of the beeper
# line is indicated by a corner that contains no beepers.
def collect_line_of_beepers():
    while beepers_present():
        pick_beeper()
        if front_is_clear():
            move()

# Drops all the beepers on the current corner.
def drop_all_beepers() :
    while beepers_in_bag():
        put_beeper()

# Returns Karel to its initial position at the corner of 1st
# Avenue and 1st row, facing east.  The precondition for this
# method is that Karel must be facing east somewhere on 1st
# row, which is true at the conclusion of collectAllBeepers.
def return_home():
    turn_around()
    move_to_wall()
    turn_around()

# Moves Karel forward until it is blocked by a wall.
def move_to_wall():
    while front_is_clear():
        move()

# Turns Karel 180 degrees around
def turn_around():
    turn_left()
    turn_left()
# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program("BeeperCollectingKarel.w")

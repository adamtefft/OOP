import random

# The Coin class simulates a coin that can
# be flipped.


class Coin:
    # The _ _init_ _ method initializes the
    # sideup data attribute with 'Heads'.
    # self is always the first parameter that we need
    # self is the instance

    # this is where we can define attributes

    def __init__(self):
        self.sideup = 'Heads'

    # The toss method generates a random number
    # in the range of 0 through 1. If the number
    # is 0, then sideup is set to 'Heads'.
    # Otherwise, sideup is set to 'Tails'.

    # We are trying to simulate tossing a coin

    def toss(self):
        if random.randint(0, 1) == 0:
            self.sideup = 'Heads'
        else:
            self.__sideup = 'Tails'
            # the __ hides the attributes
            # going forward, we always want to hide our attributes

    # toss is a mutator method which can change the value of an attribute
        # also known as a set method
        # also known as a get method (example below)
    # The get_sideup method returns the value
    # referenced by sideup.

    # the reason that you want to separate is because of reusability
    # you only want to do one thing in each method
    def get_sideup(self):
        return self.sideup

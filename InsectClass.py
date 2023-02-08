import random


class Insect:

    # this contains the first 2 attrinbutes
    def __init__(self):
        self.wings = 2
        self.legs = 4

    # this contains the third attribute
    def flight_length(self):
        self.flight = random.randint(1, 10)

    def get_flight(self):
        return self.flight

import random


class Insect:

    # this contains the first 2 attrinbutes
    def __init__(self, n, w, l):
        self.name = n
        self.wings = w
        self.legs = l
        self.flight = 0

    # this contains the third attribute
    def flight_length(self):
        self.flight = random.randint(1, 10)

    def get_flight(self):
        return self.flight

    def get_name(self):
        return self.name

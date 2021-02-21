import random


class Insect:
    def __init__(self, w, l, f):
        self.wings = w
        self.legs = l
        self.flight_length = f

    def get_flight_length(self):
        self.flight_length = random.randint(1, 10)
        return self.flight_length

    def __str__(self):
        return (
            "Wings: "
            + str(self.wings)
            + "\n"
            + "Legs: "
            + str(self.legs)
            + "\n"
            + "Flight: "
            + str(self.flight_length)
        )

"""Demostrate a raiding a refrigerator."""
from contextlib import closing

class Refrigerator:
    '''
    Raid a Refrigerator
    '''
    def open(self):
        print("Open fridge door.")

    def take(self, food):
        print("Finding {} ...".format(food))
        if food == "deep fried pizza":
            raise RuntimeError("Health Warning!!!")
        print("Taking {} ...".format(food))

    def close(self):
        print("Close fridge door.")

def raid(food):
    with closing(Refrigerator()) as r:
        r = Refrigerator()
        r.open()
        r.take(food)

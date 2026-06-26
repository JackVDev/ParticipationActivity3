"""
    dice_roll.py
    Jack Verdin
    A program created for the Participation Activity 3 in CSCC CSCI-1511
    06/26/2026
"""
import random

class Die:
    """A simple class for simulating dice rolls"""

    def __init__(self, sides):
        """Initializing the sides attribute"""
        self.sides = sides
    
    def roll_dice(self):
        print(random.randint(1, self.sides))
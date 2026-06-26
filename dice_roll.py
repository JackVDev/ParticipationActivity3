"""
    dice_roll.py
    Jack Verdin
    A program created for the Participation Activity 3 in CSCC CSCI-1511
    06/26/2026
"""
import random

class Die:
    """A simple class for simulating dice rolls"""

    def __init__(self, sides=6):
        """Initializing the sides attribute"""
        self.sides = sides
    
    def roll_dice(self):
        print(random.randint(1, self.sides))

dice_6 = Die(6)
for l in range(10):
    dice_6.roll_dice()

dice_10 = Die(10)
dice_20 = Die(20)

for l in range(10):
    dice_6.roll_dice()
    dice_10.roll_dice()
    dice_20.roll_dice()
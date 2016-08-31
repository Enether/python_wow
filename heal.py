"""
This module will hold the Heal class in the game.
The heal class holds information about the type of heal we have
"""


class Heal:
    def __init__(self, heal_amount: float=0):
        self.heal_amount = heal_amount

    def __str__(self):
        return "{0:.2f}".format(self.heal_amount)

    def __add__(self, other):
        return other + self.heal_amount

    def __radd__(self, other):
        return other + self.heal_amount

    def __iadd__(self, other: float) -> float:
        return other + self.heal_amount

    def __sub__(self, other: float) -> float:
        return self.heal_amount - other

    def __isub__(self, other: float) -> float:
        return self.heal_amount - other

    def __rsub__(self, other: float) -> float:
        return other - self.heal_amount


class NatureHeal(Heal):
    """
    The idea with nature heal is that every such heal leaves off a HoT (healing over time effect) for a % of the main heal
    """
    pass # TODO: IMPLEMENT


class HolyHeal(Heal):
    """
    The idea with holy heal is that every such heal has a significant chance to heal for double it's original amount.
    """
    DOUBLE_HEAL_CHANCE = 30  # percentage chance to double heal

    def __init__(self, heal_amount: float=0):
        super().__init__(heal_amount)
        self.will_double_heal = self.check_double_heal()  # type: bool

        if self.will_double_heal:
            # double the heal
            self.heal_amount *= 2

    def __str__(self):
        if self.will_double_heal:
            return "{0:.2f} crit".format(self.heal_amount)
        return "{0:.2f}".format(self.heal_amount)

    def check_double_heal(self) -> bool:
        """ Uses random odds to calculate if this heal should trigger it's double effect
            Chances are 30%"""
        import random
        '''
        Generate a random float from 0.0 to ~0.9999 with random.random(), then multiply it by 100
        and compare it to the double_heal_chance. If the double_heal_chance is bigger, the item has dropped.

        Example: heal chance is 30% and we roll a random float. There's a 70% chance to get a float that's bigger
        than 0.3 and a 30% chance to get a float that's smaller. We roll 0.25, multiply it by 100 = 25 and see
        that the drop chance is bigger, therefore the item should drop.
        '''
        random_float = random.random() * 100

        if random_float <= self.DOUBLE_HEAL_CHANCE:
            # we will heal for double the amount
            return True

        return False


class ProtectiveHeal(Heal):
    """
    The idea with protective heal is that every such heal leaves off a slight absorption shield on the target, absorbing
    a % of the original heal.
    """
    pass # TODO: IMPLEMENT
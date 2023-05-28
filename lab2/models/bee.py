"""
This module defines the Bee class, which represents a bee, a type of insect.
"""

from lab2.models.insect import Insect


class Bee(Insect):
    """
    A class representing a bee, which is a type of insect.
    """
    favorite_set_of_food = {"honey", "pollen"}

    def can_inject_poison(self):
        """
        Determines if a bee can inject poison.

        Returns:
            bool: True if a bee can inject poison, False otherwise.
        """
        return False

    def survive_over_winter(self):
        """
        Determines if a bee can survive over the winter.

        Returns:
            bool: True if a bee can survive over the winter, False otherwise.
        """
        return True

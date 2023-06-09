"""
This module defines the Spider class, which represents a spider, a type of insect.
"""
from lab2.models.insect import Insect


class Spider(Insect):
    """
    A class representing a Spider, which is a type of insect.

    Inherits from:
        Insect: An abstract base class for insects.
    """
    def __init__(self, name: str = "Insect", number_of_legs: int = 0, has_wings: bool = False,
                 is_dangerous: bool = False):
        super().__init__(name, number_of_legs, has_wings, is_dangerous)
        self.favorite_set_of_food = {"insect", "meat"}

    def can_inject_poison(self):
        """
        Checks if the spider can inject poison.

        Returns:
            bool: True if the spider has more than 8 legs, indicating it can inject poison. False otherwise.
        """
        return self.number_of_legs > 8

    def survive_over_winter(self):
        """
        Determines if the spider can survive over winter.

        Returns:
            bool: False, indicating that spiders typically do not survive over winter.
        """
        return False

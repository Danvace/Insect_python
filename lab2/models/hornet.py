"""
This module defines the Hornet class, which represents a Hornet, a type of insect.
"""
from lab2.models.insect import Insect


class Hornet(Insect):
    """
    A class representing a hornet, which is a type of insect.
    """



    def __init__(self, name: str = "Insect", number_of_legs: int = 0, has_wings: bool = False,
                 is_dangerous: bool = False, is_queen: bool = False,
                 is_old_queen: bool = False):

        """
        Initialize a Hornet object.

        Args:
            name (str): The name of the hornet. Default is "Insect".
            number_of_legs (int): The number of legs the hornet has. Default is 0.
            has_wings (bool): Indicates whether the hornet has wings. Default is False.
            is_dangerous (bool): Indicates whether the hornet is dangerous. Default is False.
            is_queen (bool): Indicates whether the hornet is a queen. Default is False.
            is_old_queen (bool): Indicates whether the hornet is an old queen. Default is False.
        """
        super().__init__(name, number_of_legs, has_wings, is_dangerous)
        self.is_queen = is_queen
        self.is_old_queen = is_old_queen
        self.favorite_set_of_food = {"bread", "water", "grain"}

    def can_inject_poison(self):
        """
        Check if the hornet can inject poison.

        Returns:
            bool: True if the hornet is a queen and has more than 6 legs, False otherwise.
        """
        return self.is_queen and self.number_of_legs > 6

    def survive_over_winter(self):
        """
        Check if the hornet can survive over the winter.

        Returns:
            bool: True if the hornet is not an old queen and can survive over the winter, False otherwise.
        """
        return not self.is_old_queen

    def __str__(self):
        """
        Return a string representation of the hornet.

        Returns:
            str: String representation of the hornet.
        """
        return super().__str__() + f"Hornet(is_queen = {self.is_queen}, is_old_queen = {self.is_old_queen})"

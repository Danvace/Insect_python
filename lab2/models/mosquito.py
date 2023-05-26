"""
This module defines the Mosquito class, which represents a mosquito, a type of insect.
"""
from lab2.models.insect import Insect


class Mosquito(Insect):
    """
    A class representing a mosquito, which is a type of insect.
    """

    def __init__(self, name="Insect", number_of_legs=0, has_wings=False, is_dangerous=False, has_health_sting=False):
        """
        Initialize a Mosquito object.

        Args:
            name (str): The name of the mosquito. Default is "Insect".
            number_of_legs (int): The number of legs the mosquito has. Default is 0.
            has_wings (bool): Indicates whether the mosquito has wings. Default is False.
            is_dangerous (bool): Indicates whether the mosquito is dangerous. Default is False.
            has_health_sting (bool): Indicates whether the mosquito has a health sting. Default is False.
        """
        super().__init__(name, number_of_legs, has_wings, is_dangerous)
        self.has_health_sting = has_health_sting

    def can_inject_poison(self):
        """
        Check if the mosquito can inject poison with its sting.

        Returns:
            bool: True if the mosquito has a health sting and can inject poison, False otherwise.
        """
        return self.has_health_sting

    def survive_over_winter(self):
        """
        Check if the mosquito can survive over the winter.

        Returns:
            bool: False, as mosquitoes generally do not survive over the winter.
        """
        return False

    def __str__(self):
        """
        Return a string representation of the mosquito.

        Returns:
            str: String representation of the mosquito.
        """
        return super().__str__() + f"Mosquito(has_health_sting = {self.has_health_sting})"

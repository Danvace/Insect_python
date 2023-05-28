"""
This module defines the Insect class, which represents an abstract insect.

Classes:
    Insect: An abstract base class for insects.
"""

from abc import ABC, abstractmethod


class Insect(ABC):
    """
    An abstract base class for representing an insect.

    Attributes:
        name (str): The name of the insect.
        number_of_legs (int): The number of legs the insect has.
        has_wings (bool): Indicates whether the insect has wings.
        is_dangerous (bool): Indicates whether the insect is dangerous.
    """

    def __init__(self, name: str = "Insect", number_of_legs: int = 0, has_wings: bool = False,
                 is_dangerous: bool = False):
        """
        Initializes a new instance of the Insect class.

        Args:
            name (str): The name of the insect. Default is "Insect".
            number_of_legs (int): The number of legs the insect has. Default is 0.
            has_wings (bool): Indicates whether the insect has wings. Default is False.
            is_dangerous (bool): Indicates whether the insect is dangerous. Default is False.
        """
        self.name = name
        self.number_of_legs = number_of_legs
        self.has_wings = has_wings
        self.is_dangerous = is_dangerous

    def __str__(self):
        """
        Returns a string representation of the insect object.

        Returns:
            str: A string representation of the insect object.
        """
        return f"Insect(name='{self.name}', number_of_legs={self.number_of_legs}, has_wings={self.has_wings}, " \
               f"is_dangerous={self.is_dangerous})"

    @abstractmethod
    def can_inject_poison(self):
        """
        Abstract method to check if the insect can inject poison.

        Returns:
            bool: True if the insect can inject poison, False otherwise.
        """

    @abstractmethod
    def survive_over_winter(self):
        """
        Abstract method to determine if the insect can survive over winter.

        Returns:
            bool: True if the insect can survive over winter, False otherwise.
        """

    def get_attributes_by_type(self, data_type):
        """
                Get a dictionary with all the keys and values of object attributes of a specific data type.

                Args:
                    data_type (type): The data type to filter attributes.

                Returns:
                    dict: A dictionary containing the keys and values
                    of object attributes matching the specified data type.
        """
        return {key: value for key, value in self.__dict__.items() if isinstance(value, data_type)}

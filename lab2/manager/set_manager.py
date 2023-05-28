"""
This module defines a SetManager class that manages a collection of insects and their favorite foods.
"""
from lab2.manager.insect_manager import InsectManager


class SetManager:
    """
    A class that manages a collection of insects and their favorite foods.
    """

    def __init__(self, insect_manager: InsectManager = InsectManager()):
        """
        Initialize the SetManager with an InsectManager.

        Args:
            insect_manager (InsectManager): An instance of InsectManager to manage the insects.
                Defaults to a new instance of InsectManager if not provided.
        """
        self.insect_manager = insect_manager

    def __iter__(self):
        """
        Iterate over the favorite foods of all insects in the insect manager.

        Yields:
            str: The favorite food of an insect.
        """
        for obj in self.insect_manager:
            for food in obj.get_favorite_food_set():
                yield food

    def __len__(self):
        """
        Get the total number of favorite foods across all insects.

        Returns:
            int: The total number of favorite foods.
        """
        count = 0
        for obj in self.insect_manager:
            count += len(obj.get_favorite_food_set())
        return count

    def __next__(self):
        """
        Return the next favorite food of an insect.

        Yields:
            str: The next favorite food of an insect.
        
        Raises:
            StopIteration: If there are no more favorite foods.
        """
        for obj in self.insect_manager:
            for food in obj.get_favorite_food_set():
                yield food

    def __getitem__(self, index):
        """
        Get the favorite food at the specified index.

        Args:
            index (int): The index of the favorite food to retrieve.

        Returns:
            str: The favorite food at the specified index.

        Raises:
            IndexError: If the index is out of range.
        """
        for obj in self.insect_manager:
            favorite_food_set = obj.get_favorite_food_set()
            if index < len(favorite_food_set):
                return list(favorite_food_set)[index]
            index -= len(favorite_food_set)
        raise IndexError("Index out of range")

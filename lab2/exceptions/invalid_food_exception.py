"""
Exception
"""


class InvalidFoodException(Exception):
    """Exception raised for invalid food items."""

    def __init__(self, food):
        self.food = food
        message = f"Invalid food item: {food}"
        super().__init__(message)

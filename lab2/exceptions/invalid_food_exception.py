"""
Exception
"""


class InvalidFoodException(Exception):
    """Exception raised for invalid food items."""
    message = "invalid type of food. Should be string"

    def __init__(self):
        """
        Exception for invalid type of food
        """
        super().__init__(self.message)

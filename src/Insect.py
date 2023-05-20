class Insect:
    """
    A class representing an insect.
    """

    __instance = None

    def __init__(self, name="Insect", number_of_legs=0, has_wings=False, is_dangerous=False, is_sleeping=False):
        """
        Initializes a new instance of the Insect class.

        Args:
            name (str): The name of the insect. Default is "Insect".
            number_of_legs (int): The number of legs the insect has. Default is 0.
            has_wings (bool): Indicates whether the insect has wings. Default is False.
            is_dangerous (bool): Indicates whether the insect is dangerous. Default is False.
            is_sleeping (bool): Indicates whether the insect is currently sleeping. Default is False.
        """
        self.name = name
        self.number_of_legs = number_of_legs
        self.has_wings = has_wings
        self.is_dangerous = is_dangerous
        self.is_sleeping = is_sleeping

    def is_poisonous(self):
        """
        Checks if the insect is poisonous.

        Returns:
            bool: True if the number of legs is greater than or equal to 6, False otherwise.
        """
        return self.number_of_legs >= 6

    def hibernate(self):
        """
        Puts the insect into hibernation by setting the is_sleeping attribute to True.
        """
        self.is_sleeping = True

    def wake_up(self):
        """
        Wakes up the insect from hibernation by setting the is_sleeping attribute to False.
        """
        self.is_sleeping = False

    def __str__(self):
        """
        Returns a string representation of the insect object.

        Returns:
            str: A string representation of the insect object.
        """
        return f"Insect(name='{self.name}', number_of_legs={self.number_of_legs}, has_wings={self.has_wings}, " \
               f"is_dangerous={self.is_dangerous}, is_sleeping={self.is_sleeping})"

    @staticmethod
    def get_instance():
        """
        Returns a singleton instance of the Insect class. If an instance doesn't exist, it creates one.

        Returns:
            Insect: An instance of the Insect class.
        """
        if Insect.__instance is None:
            Insect.__instance = Insect()
        return Insect.__instance

class InsectManager:
    """
    A class for managing a list of insects.
    """

    def __init__(self, list_of_insects=None):
        """
        Initialize an InsectManager object.

        Args:
            list_of_insects (list): A list of Insect objects. Default is None.
        """
        self.insects = list_of_insects

    def find_all_with_more_than(self, legs):
        """
        Find all insects with more than the specified number of legs.

        Args:
            legs (int): The minimum number of legs for the insects to be included.

        Returns:
            list: A list of Insect objects with more than the specified number of legs.
        """
        return list(filter(lambda insect: insect.number_of_legs >= legs, self.insects))

    def find_all_with_wings(self):
        """
        Find all insects that have wings.

        Returns:
            list: A list of Insect objects that have wings.
        """
        return list(filter(lambda insect: insect.has_wings, self.insects))

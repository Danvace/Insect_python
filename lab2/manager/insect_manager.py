"""
This module defines the InsectManager class for managing a list of insects.
"""


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

    def __getitem__(self, index):
        """
        Get the insect at the specified index.

        Args:
            index (int): The index of the insect to retrieve.

        Returns:
            Insect or None: The Insect object at the specified index, or None if the index is out of range.
        """
        try:
            return self.insects[index]
        except IndexError:
            return None

    def __iter__(self):
        """

        :return:  iterator for insects
        """
        return iter(self.insects)

    def __len__(self):
        """

        :return: len of insects
        """
        return len(self.insects)

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

    def list_of_result_can_inject_poison(self):
        """

        :return: list of can inject poison result
        """
        return [insect.can_inject_poison() for insect in self.insects]

    def zip_return(self):
        """

        :return: list of zip element end result of method can_inject poison
        """
        result = self.list_of_result_can_inject_poison()
        return list(zip(self.insects, result))

    def enumerate_list(self):
        """

        :return: f string of insect and index
        """
        return [f"{insect} at index {index}" for index, insect in enumerate(self.insects)]

    def dict_type(self, data_type):
        """

        :param data_type:
        :return:
        """
        return [insect.get_attributes_by_type(data_type) for insect in self.insects]

    def dict_condition_can_inject_poison(self):
        """

        :return: dict of any() and all() result
        """
        return {"any": any(self.list_of_result_can_inject_poison()),
                "all": all(self.list_of_result_can_inject_poison())}

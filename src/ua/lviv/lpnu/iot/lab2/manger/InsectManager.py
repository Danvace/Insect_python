class InsectManager:

    def __init__(self, list_of_insects=None):
        self.list_of_insects = list_of_insects

    def find_all_with_more_than(self, legs):
        return [insect for insect in self.list_of_insects if insect.number_of_legs >= legs]

    def find_all_with_wings(self):
        return [insect for insect in self.list_of_insects if insect.has_wings]

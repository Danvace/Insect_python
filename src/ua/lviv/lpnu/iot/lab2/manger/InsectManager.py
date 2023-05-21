#
# if __name__ == "__main__":
#     cockroach = Insect("cockroach", 4, True, False, False)
#     fly = Insect("fly", 6, False, False, False)
#     insects = [cockroach, fly, Insect.get_instance(), Insect.get_instance()]
#
#     for insect in insects:
#         print(insect)
#
#     s1 = Insect.get_instance()
#     s2 = Insect.get_instance()
#     print(id(s1) == id(s2))


class InsectManager:

    def __init__(self, list_of_insects=None):
        self.list_of_insects = list_of_insects

    def find_all_with_more_than(self, legs):
        return [insect for insect in self.list_of_insects if insect.number_of_legs >= legs]

    def find_all_with_wings(self):
        return [insect for insect in self.list_of_insects if insect.has_wings]
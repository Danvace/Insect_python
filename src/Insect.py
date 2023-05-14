class Insect:
    _instance = None

    def __init__(self, name="Insect", number_of_legs=0, has_wings=False, is_dangerous=False, is_sleeping=False):
        self.name = name
        self.number_of_legs = number_of_legs
        self.has_wings = has_wings
        self.is_dangerous = is_dangerous
        self.is_sleeping = is_sleeping

    def is_poisonous(self):
        return self.number_of_legs >= 6

    def hibernate(self):
        self.is_sleeping = True

    def wake_up(self):
        self.is_sleeping = False

    def __str__(self):
        return f"Insect(name='{self.name}', number_of_legs={self.number_of_legs}, has_wings={self.has_wings}, " \
               f"is_dangerous={self.is_dangerous}, is_sleeping={self.is_sleeping})"

    @staticmethod
    def get_instance():
        if Insect._instance is None:
            Insect._instance = Insect()
        return Insect._instance


if __name__ == "__main__":
    cockroach = Insect("cockroach", 4, True, False, False)
    fly = Insect("fly", 6, False, False, False)
    insects = [cockroach, fly, Insect.get_instance(), Insect.get_instance()]

    for insect in insects:
        print(insect)

    s1 = Insect.get_instance()
    s2 = Insect.get_instance()
    print(id(s1) == id(s2))
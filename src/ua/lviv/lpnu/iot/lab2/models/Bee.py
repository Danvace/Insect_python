from src.ua.lviv.lpnu.iot.lab2.models.Insect import Insect


class Bee(Insect):
    def __init__(self, name="Bee", number_of_legs=6, has_wings=True, is_dangerous=False):
        super().__init__(name, number_of_legs, has_wings, is_dangerous)

    @staticmethod
    def can_inject_poison():
        return False

    @staticmethod
    def survive_over_winter():
        return True

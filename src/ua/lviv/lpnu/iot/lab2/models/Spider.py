from src.ua.lviv.lpnu.iot.lab2.models.Insect import Insect


class Spider(Insect):
    def __init__(self, name="Spider", number_of_legs=8, has_wings=False, is_dangerous=True):
        super().__init__(name, number_of_legs, has_wings, is_dangerous)

    @staticmethod
    def can_inject_poison():
        return True

    @staticmethod
    def survive_over_winter():
        return False

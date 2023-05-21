from src.ua.lviv.lpnu.iot.lab2.models.Insect import Insect


class Hornet(Insect):

    def __init__(self, name="Insect", number_of_legs=0, has_wings=False, is_dangerous=False, is_queen=False,
                 is_old_queen=False):
        super().__init__(name, number_of_legs, has_wings, is_dangerous)
        self.is_queen = is_queen
        self.is_old_queen = is_old_queen

    def can_inject_poison(self):
        return self.is_queen and self.number_of_legs > 6

    def survive_over_winter(self):
        return not self.is_old_queen

    def __str__(self):
        return super().__str__() + \
               f"Hornet(is_queen = {self.is_queen}, is_old_queen = {self.is_old_queen})"

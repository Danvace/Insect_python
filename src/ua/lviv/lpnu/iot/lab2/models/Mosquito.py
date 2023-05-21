from src.ua.lviv.lpnu.iot.lab2.models.Insect import Insect


class Mosquito(Insect):
    def __init__(self, name="Insect", number_of_legs=0, has_wings=False, is_dangerous=False, has_health_sting=False):
        super().__init__(name, number_of_legs, has_wings, is_dangerous)
        self.has_health_sting = has_health_sting

    def can_inject_poison(self):
        return self.has_health_sting

    def survive_over_winter(self):
        return False

    def __str__(self):
        return super().__str__() +\
            f"Mosquito(has_health_sting = {self.has_health_sting})"

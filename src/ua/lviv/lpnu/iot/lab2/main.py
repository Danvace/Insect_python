from src.ua.lviv.lpnu.iot.lab2.manger.InsectManager import InsectManager
from src.ua.lviv.lpnu.iot.lab2.models.Hornet import Hornet
from src.ua.lviv.lpnu.iot.lab2.models.Mosquito import Mosquito

hornet = Hornet("Dan", 4, True, True, True)
mosquito = Mosquito("Ivanka", 6, True)
insect_manager = InsectManager([Hornet(), Mosquito(), hornet, mosquito])

for insect in insect_manager.list_of_insects:
    print(insect)

print("\n")

list_A = insect_manager.find_all_with_wings()

for insect in list_A:
    print(insect)

print("\n")

list_B = insect_manager.find_all_with_more_than(5)

for insect in list_B:
    print(insect)

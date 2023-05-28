"""
This script demonstrates the usage of the InsectManager class and various insect models.

The InsectManager class is responsible for managing a collection of insects and provides methods
to find insects based on certain criteria.

The insect models include Bee, Hornet, Mosquito, and Spider, each representing
a specific type of insect with different attributes.

Usage:
- Create instances of different insect models.
- Initialize an InsectManager instance with a list of insects.
- Use the InsectManager methods to find and retrieve specific insects.
- Print the insects based on the search criteria.

Note: The actual implementations of the InsectManager class and the insect models are assumed to be
defined in separate files.
"""
from lab2.manager.insect_manager import InsectManager
from lab2.models.bee import Bee
from lab2.models.hornet import Hornet
from lab2.models.mosquito import Mosquito
from lab2.models.spider import Spider

# Create instances of different insects
hornet = Hornet("Dan", 9, True, True, True)
mosquito = Mosquito("Ivanka", 6, True, True)
spider = Spider("Vitalik", 8, False, False)

# Create an instance of the InsectManager and initialize it with a list of insects
insect_manager = InsectManager([Hornet(), Mosquito(), hornet, mosquito, spider, Bee()])

# Print all the insects in the InsectManager
# for insect in insect_manager.insects:
#     print(insect)
#
# print("\n")
#
# # Find all insects with wings
# list_A = insect_manager.find_all_with_wings()
#
# # Print the insects with wings
# for insect in list_A:
#     print(insect)
#
# print("\n")
#
# # Find all insects with more than 5 legs
# list_B = insect_manager.find_all_with_more_than(5)
#
# # Print the insects with more than 5 legs
# for insect in list_B:
#     print(insect)
#
# print("\n")

# a = insect_manager.zip_return()
#
# for i in a:
#     print(i[0])
#     print(i[1])
#
# b = insect_manager.dict_type(bool)
# for j in b:
#     print(j)

print(insect_manager.list_of_result_can_inject_poison())
c = insect_manager.dict_condition_can_inject_poison()
print(c)

a = insect_manager.list_of_result_can_inject_poison()
print(a)

b = insect_manager.zip_return()
c = set(insect_manager.zip_return())

d = insect_manager.enumerate_list()
f = insect_manager.enumerate_list()
u = insect_manager.enumerate_list()

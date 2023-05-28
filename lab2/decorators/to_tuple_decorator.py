"""
    decorator function
"""


def to_tuple_decorator(iterator_method):
    """
       Decorator that converts the output of an iterator method into a tuple.

       Args:
           iterator_method (function): The iterator method to be decorated.

       Returns:
           function: The decorated method.
    """

    def inner(*args, **kwargs):
        # Викликати оригінальний метод-ітератор
        iterator = iterator_method(*args, **kwargs)

        # Перетворити результат в кортеж
        result = tuple(iterator)

        return result

    return inner

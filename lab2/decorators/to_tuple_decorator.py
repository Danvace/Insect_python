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
        return tuple(iterator_method(*args, **kwargs))

    return inner

"""
 decorator to count calls of function
"""


def method_calls_counter(file_path):
    """

    :param file_path: the file path where save data
    :return: Function
    """

    def decorator(func):
        def wrapper(*args, **kwargs):

            try:
                with open(file_path, 'r', encoding="UTF-8") as file:
                    lines = file.readlines()
            except FileNotFoundError:
                lines = []

            method_name = func.__name__
            call_count = 1
            for i, line in enumerate(lines):
                if line.startswith(f'{method_name},'):
                    call_count = int(line.split(',')[1]) + 1
                    lines[i] = f'{method_name},{call_count}\n'
                    break
            else:

                lines.append(f'{method_name},{call_count}\n')

            with open(file_path, 'w', encoding="UTF-8") as file:
                file.writelines(lines)

            return func(*args, **kwargs)

        return wrapper

    return decorator

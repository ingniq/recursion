# 1. Возведение числа "number" в степень "power"
def raise_to_power(number: int, power: int) -> int:
    if power > 1:
        return number * raise_to_power(number, power - 1)

    return number


# 2. вычисление суммы цифр числа;
def calc_sum_of_digits_of(number: int) -> int:
    if number >= 10:
        digit = number % 10
        number = number // 10

        return digit + calc_sum_of_digits_of(number)

    return number


# 3. расчёт длины списка, для которого разрешена только операция удаления первого элемента pop(0) (и получение длины конечно);
def calc_list_length(value: list) -> int:
    if value:
        value.pop()
        return 1 + calc_list_length(value)

    return 0


# 4. проверка, является ли строка палиндромом;
def is_palindrome(value: str) -> bool:
    if len(value) in [0, 1]:
        return True

    if value[0] != value[-1]:
        return False

    return is_palindrome(value[1:-1])


# 5. печать только чётных значений из списка;
def print_even_values_from(list_values: list) -> None:
    __printing_even_list_values(list_values=list_values, start_index=0)

def __printing_even_list_values(*, list_values, start_index):
    if start_index >= len(list_values):
        return

    if list_values[start_index] % 2 == 0:
        print(list_values[start_index])

    __printing_even_list_values(list_values=list_values, start_index=start_index + 1)


# 6. печать элементов списка с чётными индексами;
def print_values_with_even_indexes(list_values: list) -> None:
    __printing_list_values(list_values=list_values, start_index=0, step=2)

def __printing_list_values(*, list_values, start_index, step):
    if start_index >= len(list_values):
        return

    print(list_values[start_index])
    __printing_list_values(list_values=list_values, start_index=start_index + step, step=step)


# 7. нахождение второго максимального числа в списке (с учётом, что максимальных может быть несколько, если они равны).
def get_second_max_number_in(list_values: list) -> int:
    first_max, second_max = list_values[0], list_values[1]

    if list_values[1] > list_values[0]:
        first_max, second_max = list_values[1], list_values[0]

    return __find_second_max_number(list_values=list_values, index=2, first_max=first_max, second_max=second_max)

def __find_second_max_number(*, list_values: list, index: int, first_max: int, second_max: int) -> int:
    if index >= len(list_values):
        return second_max

    if list_values[index] > first_max:
        second_max, first_max = first_max, list_values[index]
    elif list_values[index] > second_max:
        second_max = list_values[index]

    return __find_second_max_number(list_values=list_values, index=index + 1,  first_max=first_max, second_max=second_max)


from os import listdir
from os.path import isfile, join

# 8. поиск всех файлов в заданном каталоге, включая файлы, расположенные в подкаталогах произвольной вложенности.
def get_list_of_files_recursively(path: str) -> list:
    dir_items = listdir(path)

    return __collect_list_of_files(path=path, dir_items=dir_items, index=0)


def __collect_list_of_files(*, path, dir_items, index):
    if index >= len(dir_items):
        return []

    file_names = []
    list_item = join(path, dir_items[index])

    if isfile(list_item):
        file_names.append(dir_items[index])
    else:
        file_names = __collect_list_of_files(path=list_item, dir_items=listdir(list_item), index=0)

    return file_names + __collect_list_of_files(path=path, dir_items=dir_items, index=index + 1)



# Повышенная сложность. Генерация всех корректных сбалансированных комбинаций круглых скобок (параметр -- количество открывающих скобок).
def generate_balanced_parentheses(num_of_opening_parentheses: int) -> None:
    pass

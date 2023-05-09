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
    if not list_values:
        return

    value = list_values.pop(0)

    if value % 2 == 0:
        print(value)

    print_even_values_from(list_values)


# 6. печать элементов списка с чётными индексами;
def print_values_with_even_indexes(value: list) -> None:
    pass


# 7. нахождение второго максимального числа в списке (с учётом, что максимальных может быть несколько, если они равны).
def get_second_max_number_in(value: list) -> int:
    pass


# 8. поиск всех файлов в заданном каталоге, включая файлы, расположенные в подкаталогах произвольной вложенности.
def get_list_of_files_recursively(path: str) -> list:
    pass


# Повышенная сложность. Генерация всех корректных сбалансированных комбинаций круглых скобок (параметр -- количество открывающих скобок).
def generate_balanced_parentheses(num_of_opening_parentheses: int) -> None:
    pass

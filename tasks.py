# 1. Возведение числа "number" в степень "power"

def raise_to_power(*, number: int, power: int) -> int:
    if not isinstance(number, int) or not isinstance(power, int) :
        raise ValueError("Only integers are allowed")

    if number == power == 0:
        raise ValueError("Not defined")

    if power == 0:
        return 1

    if power < 0:
        number = 1/number
        power *= -1

    def multiply(number, power, product):
        if power == 1:
            return product

        return multiply(number, power - 1, product * number)

    return multiply(number, power, number)

# 2. вычисление суммы цифр числа;

def calc_sum_of_digits_of(number: int) -> int:
    pass

# 3. расчёт длины списка, для которого разрешена только операция удаления первого элемента pop(0) (и получение длины конечно);

def calc_list_length(value: list) -> int:
    pass

# 4. проверка, является ли строка палиндромом;

def is_palindrome(value: str) -> bool:
    pass

# 5. печать только чётных значений из списка;

def print_even_values_from(value: list) -> None:
    pass

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

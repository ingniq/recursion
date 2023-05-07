import pytest
from tasks import *

@pytest.mark.parametrize(
    "number, power, expected", [
    (None, None, "Only numbers are allowed"),
    (None, 2, "Only numbers are allowed"),
    (2, None, "Only numbers are allowed"),
    ("2", "2", "Only numbers are allowed"),
    (2, "2", "Only numbers are allowed"),
    ("2", 2, "Only numbers are allowed"),
    (-2, -2, 0.25),
    (-2, -1, -0.5),
    (-2, 0, 1),
    (-2, 1, -2),
    (-2, 2, 4),
    (-2, 3, -8),
    (-1, -2, 1),
    (-1, -1, -1),
    (-1, 0, 1),
    (-1, 1, -1),
    (-1, 2, 1),
    (0, -2, 0),
    (0, 0, 0),
    (0, 2, 0),
    (1, -2, 1),
    (1, 0, 1),
    (1, 2, 1),
    (2, 0, 1),
    (2, 1, 2),
    (2, 2, 4),
    (2, 3, 8),
    (2.5, 3, 15.625),
    (2.5, 2.5, 9.882),
])
def test_raise_to_power(number, power, expected):
    if not isinstance(number, int) or not isinstance(power, int):
        with pytest.raises(Exception) as e:
            raise_to_power(number=number, power=power)
        assert e.value == expected
        assert e.type == ValueError
    else:
        assert expected == raise_to_power(number=number, power=power)

def test_calc_sum_of_digits_of():
    pass

def test_calc_list_length():
    pass

def test_is_palindrome():
    pass

def test_print_even_values_from():
    pass

def test_print_values_with_even_indexes():
    pass

def test_get_second_max_number_in():
    pass

def test_get_list_of_files_recursively():
    pass

def test_generate_balanced_parentheses():
    pass

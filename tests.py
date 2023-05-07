import pytest
from tasks import *

@pytest.mark.parametrize(
    "number, power, expected", [
    (None, None, "Only integers are allowed"),
    (None, 2, "Only integers are allowed"),
    (2, None, "Only integers are allowed"),
    ("2", "2", "Only integers are allowed"),
    (2, "2", "Only integers are allowed"),
    ("2", 2, "Only integers are allowed"),
    (0, -2, "division by zero"),
    (0, 0, "Not defined"),
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
    (0, 2, 0),
    (1, -2, 1),
    (1, 0, 1),
    (1, 2, 1),
    (2, 0, 1),
    (2, 1, 2),
    (2, 2, 4),
    (2, 3, 8),
])
def test_raise_to_power(number, power, expected):
    is_value_error = not isinstance(number, int) or not isinstance(power, int) or (power == number == 0)
    is_zero_division = (number == 0 and power < 0)

    if is_value_error:
        with pytest.raises(ValueError) as e:
            raise_to_power(number=number, power=power)
            assert e.type == ValueError
            assert e.value == expected
    elif is_zero_division:
        with pytest.raises(ZeroDivisionError) as e:
            raise_to_power(number=number, power=power)
            assert e.type == ZeroDivisionError
            assert e.value == expected
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

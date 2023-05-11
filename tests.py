import pytest
from tasks import *

@pytest.mark.parametrize(
    "number, power, expected", [
    # (None, None, "Only integers are allowed"),
    # (None, 2, "Only integers are allowed"),
    # (2, None, "Only integers are allowed"),
    # ("2", "2", "Only integers are allowed"),
    # (2, "2", "Only integers are allowed"),
    # ("2", 2, "Only integers are allowed"),
    # (0, -2, "division by zero"),
    # (0, 0, "Not defined"),
    # (-2, -2, 0.25),
    # (-2, -1, -0.5),
    # (-2, 0, 1),
    # (-1, -2, 1),
    # (-1, -1, -1),
    # (-1, 0, 1),
    # (1, -2, 1),
    # (1, 0, 1),
    # (2, 0, 1),
    (-2, 1, -2),
    (-2, 2, 4),
    (-2, 3, -8),
    (-1, 1, -1),
    (-1, 2, 1),
    (0, 2, 0),
    (1, 2, 1),
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
            assert e.value == expected
    elif is_zero_division:
        with pytest.raises(ZeroDivisionError) as e:
            raise_to_power(number=number, power=power)
            assert e.value == expected
    else:
        assert expected == raise_to_power(number=number, power=power)


@pytest.mark.parametrize(
    "number, expected", [
    # (None, "Only integers are allowed"),
    # ("", "Only integers are allowed"),
    # ("222", "Only integers are allowed"),
    # (-123, 6),
    (0, 0),
    (1, 1),
    (10, 1),
    (100, 1),
    (110, 2),
    (101, 2),
    (111, 3),
    (123, 6),
])
def test_calc_sum_of_digits_of(number, expected):
    if not isinstance(number, int):
        with pytest.raises(ValueError) as e:
            calc_sum_of_digits_of(number=number)
            assert e.value == expected
    else:
        assert expected == calc_sum_of_digits_of(number)


@pytest.mark.parametrize(
    "input, expected", [
    (list(("a","b","c")), 3),
    (list(), 0),
])
def test_calc_list_length(input, expected):
    assert expected == calc_list_length(input)


@pytest.mark.parametrize(
    "input, expected", [
    ("a", True),
    ("abba", True),
    ("abbaabba", True),
    ("abbc", False),
    ("abc", False),
])
def test_is_palindrome(input, expected):
    assert expected == is_palindrome(input)


@pytest.mark.parametrize(
    "input, expected", [
    (list((1, 2, 3, 4)), "2\n4\n"),
    (list((1, 21, 32, 44)), "32\n44\n"),
])
def test_print_even_values_from(input, expected, capsys):
    print_even_values_from(input)
    captured = capsys.readouterr()
    assert captured.out == expected


@pytest.mark.parametrize(
    "input, expected", [
    (list((1, 2, 3, 4)), "1\n3\n"),
    (list((1, 21, 32, 44)), "1\n32\n"),
    (list((1, 21, 32, 44, 12)), "1\n32\n12\n"),
])
def test_print_values_with_even_indexes(input, expected, capsys):
    print_values_with_even_indexes(input)
    captured = capsys.readouterr()
    assert captured.out == expected


@pytest.mark.parametrize(
    "input, expected", [
    (list((1, 3, 5)), 3),
    (list((5, 3, 5)), 5),
    (list((1, 6, 5)), 5),
    (list((6, 1, 5)), 5),
    (list((1, 6, 5, 1, 3, 5)), 5),
    (list((1, 6, 5, 1, 6, 5)), 6),
    (list((1, 6, 5, 1, 6, 6)), 6),
])
def test_get_second_max_number_in(input, expected):
    assert expected == get_second_max_number_in(input)

@pytest.mark.parametrize(
    "input, expected", [
    (
        "test_tree_of_files_and_directories",
        [
            "test_1_file_1.txt",
            "test_1_1_file_1.txt",
            "test_2_file_2.py",
            "test_2_file_1.txt"
        ]
    ),
])
def test_get_list_of_files_recursively(input, expected):
    assert expected == get_list_of_files_recursively(input)


def test_generate_balanced_parentheses():
    pass

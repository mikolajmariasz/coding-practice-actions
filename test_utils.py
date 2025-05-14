import pytest
import utils

@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (2, 3, 5), (3, 4, 7), (4, 5, 9)])
def test_add(a, b, expected):
    result = utils.add(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a, b, expected", [(1, 2, -1), (2, 3, -1), (3, 4, -1), (4, 5, -1)]
)
def test_subtract(a, b, expected):
    result = utils.subtract(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a, b, expected", [(1, 2, 2), (2, 3, 6), (3, 4, 12), (4, 5, 20)]
)
def test_multiply(a, b, expected):
    result = utils.multiply(a, b)
    assert result == expected


@pytest.mark.parametrize("a, b, expected", [(1, 2, 0.5), (3, 4, 0.75), (4, 5, 0.8)])
def test_divide(a, b, expected):
    result = utils.divide(a, b)
    assert result == expected

@pytest.mark.parametrize("n, expected", [
    (0, '0b0'),
    (1, '0b1'),
    (2, '0b10'),
    (100, '0b1100100'),
])
def test_binary_conversion_valid(n, expected):
    assert to_binary(n) == expected

@pytest.mark.parametrize("n", [-1, 101, 1000])
def test_binary_out_of_range(n):
    with pytest.raises(ValueError, match="Liczba poza dozwolonym zakresem"):
        to_binary(n)

@pytest.mark.parametrize("n", [1.5, 10.1, 99.9])
def test_binary_not_integer(n):
    with pytest.raises(TypeError, match="Liczba nie jest liczbą naturalną"):
        to_binary(n)
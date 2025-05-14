# Exemplary calculator functions

"""Utility functions for basic calculator operations."""


def add(a: int, b: int) -> int:
    """Return the sum of a and b."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Return the difference between a and b."""
    return a - b


def multiply(a: int, b: int) -> int:
    """Return the product of a and b."""
    return a * b


def divide(a: int, b: int) -> float:
    """Return the quotient of a divided by b."""
    return a / b

def to_binary(n):
    """Return the binary of number n."""
    if not isinstance(n, int):
        raise TypeError("Number is not natural")
    if n < 0 or n > 100:
        raise ValueError("Number is out of range")
    return bin(n)
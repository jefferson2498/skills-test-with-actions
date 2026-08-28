import sys
from pathlib import Path

# Añadir el directorio raíz al path para que reconozca el módulo src
sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest
from src.calculations import area_of_circle, get_nth_fibonacci


def test_area_of_circle():
    """Test standard area calculation."""
    assert area_of_circle(0) == 0
    assert area_of_circle(1) == 3.141592653589793


def test_area_of_circle_negative_radius():
    """Test with a negative radius to raise ValueError."""
    radius = -1
    with pytest.raises(ValueError):
        area_of_circle(radius)


def test_get_nth_fibonacci_first_values():
    """Test the base cases of the Fibonacci sequence."""
    assert get_nth_fibonacci(0) == 0
    assert get_nth_fibonacci(1) == 1
    assert get_nth_fibonacci(2) == 1


def test_get_nth_fibonacci_ten():
    """Test with n=10."""
    n = 10
    result = get_nth_fibonacci(n)
    assert result == 55


def test_get_nth_fibonacci_negative():
    """Test with a negative number to raise ValueError."""
    n = -1
    with pytest.raises(ValueError):
        get_nth_fibonacci(n)
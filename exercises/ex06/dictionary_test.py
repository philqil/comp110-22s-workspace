"""Test the dictioanry."""
__author__ = "730529618"

from dictionary import invert, favorite_color, count


def test_invert_empty() -> None:
    """Test invert w empty list."""
    a = {}
    assert invert(a) == {}


def test_invert_one() -> None:
    """Test invert w one element."""
    a = {"apple": "cat"}
    assert invert(a) == {"cat": "apple"}


def test_invert_many() -> None:
    """Test invert w multiple elements."""
    a = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(a) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_favorite_color_empty() -> None:
    """Test favorite color w  an empty dict."""
    a = {}
    assert favorite_color(a) == ""


def test_favorite_color_one() -> None:
    """Test favorite color w one element."""
    a = {"Mike": "Blue"}
    assert favorite_color(a) == "Blue"


def test_favorite_color_many() -> None:
    """Test favorite color w many elements"""
    a = {"Mike": "Red", "Nick": "Blue", "Nancy": "Blue"}
    assert favorite_color(a) == "Blue"


def test_count_empty() -> None:
    """Test count w empty list."""
    a = []
    assert count(a) == {}


def test_count_one() -> None:
    """Test count w one element."""
    a = ["apple"]
    assert count(a) == {"apple": 1}


def test_count_many() -> None:
    """Test count w many elements."""
    a = ["apple", "apple", "apple", "Nike"]
    assert count(a) == {"apple": 3, "Nike": 1}
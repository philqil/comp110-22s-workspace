"""Test the utils function."""
__author__ = "730529618"

from utils import only_evens
from utils import sub
from utils import concat


def test_only_evens_empty() -> None:
    """Test only_evens with empty set."""
    xs: list[int] = []
    assert only_evens(xs) == list()


def test_only_evens_one() -> None:
    """Test only_evens with one element."""
    xs: list[int] = [2]
    assert only_evens(xs) == [2]


def test_only_evens_many() -> None:
    """Test only_evens with many elements."""
    xs: list[int] = [1, 2, 5, 6, 8, 22, 32]
    assert only_evens(xs) == [2, 6, 8, 22, 32]


def test_sub_empty() -> None:
    """Test sub w empty set."""
    xs: list[int] = []
    assert sub(xs, 0, 0) == list()


def test_sub_one() -> None:
    """Test sub w one element."""
    xs = [1]
    assert sub(xs, 2, 1) == list()


def test_sub_many() -> None:
    """Test sub w many elements."""
    xs = [10, 20, 30, 40, 50]
    assert sub(xs, -1, 4) == [10, 20, 30, 40]


def test_concat_empty() -> None:
    """Test concat with empty sets."""
    xs: list[int] = []
    ys: list[int] = []
    assert concat(xs, ys) == list()


def test_concat_one() -> None:
    """Test concat with one element."""
    xs = [1]
    ys = [2]
    assert concat(xs, ys) == [1, 2]


def test_concat_many() -> None:
    """Test concat w many elements."""
    xs = [1, 2, 4, 5]
    ys = [2, 3, 5, 7]
    assert concat(xs, ys) == [1, 2, 4, 5, 2, 3, 5, 7]
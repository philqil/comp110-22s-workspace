"""Test the utils function."""
__author__ = "730529618"

from utils import only_evens
from utils import sub
from utils import concat


def test_only_evens_empty() -> None:
    xs = []
    assert only_evens(xs) == list()


def test_only_evens_one() -> None:
    xs = [2]
    assert only_evens(xs) == [2]


def test_only_evens_many() -> None:
    xs = [1, 2, 5, 6, 8, 22, 32]
    assert only_evens(xs) == [2, 6, 8, 22, 32]


def test_sub_empty() -> None:
    xs = []
    assert sub(xs, 0, 1) == list()


def test_sub_one() -> None:
    xs = [1]
    assert sub(xs, 2, 1) == list()


def test_sub_many() -> None:
    xs = [10, 20, 30, 40, 50]
    assert sub(xs, -1, 4) == [10, 20, 30, 40]


def test_concat_empty() -> None:
    xs = []
    ys = []
    assert concat(xs, ys) == list()


def test_concat_one() -> None:
    xs = [1]
    ys = [2]
    assert concat(xs, ys) == [1, 2]


def test_concat_many() -> None:
    xs = [1, 2, 4, 5]
    ys = [2, 3, 5, 7]
    assert concat(xs, ys) == [1, 2, 4, 5, 2, 3, 5, 7]
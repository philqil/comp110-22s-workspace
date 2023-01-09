"""Tests for linked list utils."""

import pytest
from linked_list import Node, last, linkify, value_at, max, scale, is_equal

__author__ = "730529618"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_empty() -> None:
    """Test value at with an empty list."""
    with pytest.raises(IndexError):
        value_at(None, 0)


def test_value_at_non_empty() -> None:
    """Test value with non empty list."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert value_at(linked_list, 2) == 3


def test_max_at_empty() -> None:
    """Test max with empty."""
    with pytest.raises(ValueError):
        max(None)


def test_max_at_non_empty() -> None:
    """Test max with non empty."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert max(linked_list) == 3


def test_linkify_at_empty() -> None:
    """Test linkify with none."""
    assert linkify([]) is None


def test_linkify_at_non_empty() -> None:
    """Test linkify with a list."""
    assert is_equal((linkify([1, 2, 3])), Node(1, Node(2, Node(3, None))))


def test_scale_at_empty() -> None:
    """Test scale with None."""
    assert scale(None, factor=1) is None


def test_scale_at_non_empty() -> None:
    """Test scale with a node."""
    assert is_equal(scale(linkify([1, 2, 3]), 2), Node(2, Node(4, Node(6, None))))
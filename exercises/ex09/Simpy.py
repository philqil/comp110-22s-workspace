"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730529618"


class Simpy:
    """Make a class called Simpy."""

    values: list[float]

    def __init__(self, values: list[float]) -> None:
        """Construct and object."""
        self.values = values

    def __str__(self) -> str:
        """Make a string return."""
        return f"Simpy({self.values})"

    def fill(self, num: float, times: int) -> None:
        """Fill it the list for me."""
        result = []
        i = 0
        while i < times:
            result.append(num)
            i += 1
        self.values = result
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Make a range."""
        assert step != 0.0
        result = []
        if start < stop:
            while start < stop:
                result.append(start)
                start += step
        else:
            while start > stop:
                result.append(start)
                start += step
        self.values = result

    def sum(self) -> float:
        """Sum up the values in the list."""
        result = sum(self.values)
        return result

    def __add__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Add two Simpy together."""
        i = 0
        sum = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            while i < len(self.values):
                result = self.values[i] + rhs.values[i]
                sum.append(result)
                i += 1
        else:
            for item in self.values:
                item += rhs
                sum.append(item)
        new = Simpy([])
        new.values = sum
        return new
    
    def __pow__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Take the exponential calculation."""
        i = 0
        sum = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            while i < len(self.values):
                result = self.values[i] ** rhs.values[i]
                sum.append(result)
                i += 1
        else:
            for item in self.values:
                item **= rhs
                sum.append(item)
        new = Simpy([])
        new.values = sum
        return new

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Produce a mask."""
        i = 0
        result = []
        if isinstance(rhs, Simpy):
            while i < len(self.values):
                if self.values[i] == rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
                i += 1

        else:
            for item in self.values:
                if item == rhs:
                    result.append(True)
                else:
                    result.append(False)
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Make a mask."""
        i = 0
        result: list[bool] = []
        if isinstance(rhs, Simpy):
            while i < len(self.values):
                if self.values[i] > rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
                i += 1

        else:
            for item in self.values:
                if item > rhs:
                    result.append(True)
                else:
                    result.append(False)
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Make a filter."""
        result: list[float] = []
        i = 0
        if isinstance(rhs, list):
            while i < len(self.values):
                if rhs[i] is True:
                    result.append(self.values[i])
                i += 1
        
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            new = Simpy([])
            new.values = result
            return new
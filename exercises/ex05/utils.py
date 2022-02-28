"""Write a utils function."""
__author__ = "730529618"


def only_evens(xs: list[int]) -> list[int]:
    """Print out only even numbers."""
    a_list: list[int] = list()
    for num in xs:
        if num % 2 == 0:
            a_list.append(num)
    return a_list


def sub(xs: list[int], i: int, i2: int) -> list[int]:
    """Make a sublist."""
    a_list: list[int] = list()
    if len(xs) == 0:
        return a_list
    elif i <= 0:
        i = 0
        while i < i2:
            a_list.append(xs[i])
            i += 1
        return a_list
    elif i2 > len(xs):
        i2 = len(xs)
        while i < i2:
            a_list.append(xs[i])
            i += 1
        return a_list
    elif (i > len(xs) or i2 <= 0):
        return a_list
    else:
        while i < i2:
            a_list.append(xs[i])
            i += 1
        return a_list
    return a_list


def concat(xs: list[int], ys: list[int]) -> list[int]:
    """Add two lists together."""
    a_list = list()
    for i in xs:
        a_list.append(i)
    for item in ys:
        a_list.append(item)
    return a_list
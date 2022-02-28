"""This is supposed to be a dictionary."""
__author__ = "730529618"


def invert(a: dict[str, str]) -> dict[str, str]:
    result: dict[str, str] = {}
    for key in a:
        result[a[key]] = key
    return result


def favorite_color(a: dict[str, str]) -> str:
    color_dict: dict[str, int] = {}
    for key in a:
        if a[key] in color_dict:
            color_dict[a[key]] += 1
        else:
            color_dict[a[key]] = 1
    max: int = 0
    color = ""
    for colors in color_dict:
        if color_dict[colors] > max:
            max = color_dict[colors]
            color = colors
    return color


def count(a: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}
    for i in a:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result
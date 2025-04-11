"""Docstring"""

__author__ = "730568756"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverting a dictionary of strings."""
    result = {}
    for key in dictionary:
        value = dictionary[key]
        if value in result:
            raise KeyError("Duplicate value!")
        result[value] = key
    return result


def count(values: list[str]) -> dict[str, int]:
    """Counts the frequency of an item in the given list."""
    result = {}
    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def favorite_color(colors: dict[str, str]) -> str:
    """Returns the most popular color from a dictionary of names and favorite colors."""
    result = {}
    color_list = []
    for name in colors:
        color_list.append(colors[name])
    result = count(color_list)
    for color in result:
        final = result[color]
    for color in result:
        if result[color] > final:
            final = result[color]
    for color in result:
        if result[color] == final:
            return color
    return ""


def bin_len(bins: list[str]) -> dict[int, set[str]]:
    """Returns a dictionary with the lengths of strings in a given list."""
    result = {}
    for words in bins:
        if len(words) in result:
            result[len(words)].add(words)
        else:
            result[len(words)] = {words}
    return result

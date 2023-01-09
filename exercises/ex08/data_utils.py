"""Dictionary related utility functions."""

__author__ = "730529618"

# Define your functions below
from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the csv rows into a table."""
    result: list[dict[str, str]] = []

    file_handle = open(filename, "r", encoding="utf8")

    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)

    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform rows into columns."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(data: dict[str, list[str]], rows: int) -> dict[str, list[str]]:
    """Check the first few rows."""
    result: dict[str, list[str]] = {}
    for columns in data:
        values: list[str] = []
        i = 0    
        while i < rows:
            values.append(data[columns][i])
            i += 1
        result[columns] = values

    return result


def select(table: dict[str, list[str]], column: list[str]) -> dict[str, list[str]]:
    """Check selected columns."""
    result: dict[str, list[str]] = {}
    for items in column:
        result[items] = table[items]
    
    return result


def concat(table: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Concat two dictionaries."""
    result: dict[str, list[str]] = {}
    for columns in table:
        result[columns] = table[columns]
    for items in table2:
        if items in result:
            for values in table2[items]:
                result[items].append(values)
        else:
            result[items] = table2[items]
    
    return result


def count(ls: list[str]) -> dict[str, int]:
    """Count the frequencies of occruence."""
    result: dict[str, int] = {}
    for item in ls:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result
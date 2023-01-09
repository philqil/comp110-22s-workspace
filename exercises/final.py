def merge_lists(a: list[str], b: list[int]) -> dict[str, int]:
    result: dict[str, int] = {}

    i = 0
    while i < len(a):
        result[a[i]] = b[i]
        i += 1

    return result


print(merge_lists(['blue', 'yellow', 'red'], [5, 2, 4]))
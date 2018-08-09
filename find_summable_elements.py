#!/usr/bin/env python3

from itertools import combinations
from operator import add, eq
from functools import reduce
from collections import Counter
from operator import mul
from fractions import Fraction
from contextlib import suppress


def find_summable_elements_crude(arr, target):
    def sorted_pair(pair):
        return tuple(sorted(list(pair)))
    # return sorted(
    #     [sorted_pair((a, b)) for a, b in combinations(arr, 2) if a + b == target]
    # )
    # return sorted(
    #     [sorted_pair(pair) for pair in combinations(arr, 2) if eq(add(*pair), target)]
    # )
    return sorted(
        map(
            sorted_pair,
            filter(lambda pair: eq(target, add(*pair)), combinations(arr, 2)),
        )
    )


# Not working. Needs to account for repeats of a number.
def find_summable_elements(arr, target):
    arr = sorted(arr)
    results = set()

    # Forwards
    front, back = 0, len(arr) - 1
    while front < back:
        if arr[front] + arr[back] < target:
            front += 1
            continue
        if arr[front] + arr[back] == target:
            results.add((front, back))
        back -= 1

    # Backwards
    front, back = -len(arr), -1
    while front < back:
        if arr[front] + arr[back] < target:
            front += 1
            continue
        if arr[front] + arr[back] == target:
            results.add((len(arr) + front, len(arr) + back))
        back -= 1
    return sorted([(arr[f], arr[b]) for f, b in results])


def nCk(n, k):
    return int(reduce(mul, (Fraction(n - i, i + 1) for i in range(k)), 1))


def find_summable_elements_counter(arr, target):
    d = sorted(Counter(arr).items())
    front, back = 0, len(d) - 1
    results = []
    while front <= back:
        (a, a_count), (b, b_count) = d[front], d[back]
        if a + b < target:
            front += 1
            continue
        if a + b == target:
            count = (a_count * b_count) if a != b else nCk(a_count, 2)
            results += [(a, b)] * count
        back -= 1
    return results


def find_summable_elements_counter_iter(arr, target):
    d = sorted(Counter(arr).items())
    forwards, backwards = iter(d), iter(reversed(d))
    results = []
    with suppress(StopIteration):
        (a, a_count), (b, b_count) = next(forwards), next(backwards)
        while a <= b:
            if a + b < target:
                a, a_count = next(forwards)
                continue
            if a + b == target:
                count = (a_count * b_count) if a != b else nCk(a_count, 2)
                results += [(a, b)] * count
            b, b_count = next(backwards)
    return results


fse = find_summable_elements
fse = find_summable_elements_crude
# fse = find_summable_elements_counter
# fse = find_summable_elements_counter_iter


def test_empty():
    assert fse([], 9) == []


def test_two_no_results():
    assert fse([4, 7], 9) == []


def test_two_one_result():
    assert fse([4, 5], 9) == [(4, 5)]
    assert fse([5, 4], 9) == [(4, 5)]


def test_simple():
    assert fse([1, 2, 4, 6, 9, 10], 10) == [(1, 9), (4, 6)]


def test_duplicates():
    assert fse([1, 1, 9, 9], 10) == [(1, 9), (1, 9), (1, 9), (1, 9)]
    assert fse([1, 9, 9], 10) == [(1, 9), (1, 9)]


def test_half_value():
    assert fse([5], 10) == []
    assert fse([5, 5], 10) == [(5, 5)]
    assert fse([5, 5, 5], 10) == [(5, 5), (5, 5), (5, 5)]
    assert fse([5, 5, 5, 5], 10) == [(5, 5), (5, 5), (5, 5), (5, 5), (5, 5), (5, 5)]


def test_negative_values():
    assert fse([-1, 5, 11], 10) == [(-1, 11)]
    assert fse([-1, -2], -3) == [(-2, -1)]

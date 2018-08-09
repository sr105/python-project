#!/usr/bin/env python3

from find_summable_elements import fse


def test_empty():
    assert(fse([], 9) == [])

def test_two_no_results():
    assert(fse([4, 7], 9) == [])

def test_two_one_result():
    assert(fse([4, 5], 9) == [(4, 5)])
    assert(fse([5, 4], 9) == [(4, 5)])

def test_simple():
    assert(fse([1, 2, 4, 6, 9, 10], 10) == [(1, 9), (4, 6)])

def test_duplicates():
    assert(fse([1, 1, 9, 9], 10) == [(1, 9), (1, 9), (1, 9), (1, 9)])
    assert(fse([1, 9, 9], 10) == [(1, 9), (1, 9)])


def test_half_value():
    assert(fse([5], 10) == [])
    assert(fse([5, 5], 10) == [(5, 5)])
    assert(fse([5, 5, 5], 10) == [(5, 5), (5, 5), (5, 5)])
    assert(fse([5, 5, 5, 5], 10) == [(5, 5), (5, 5), (5, 5), (5, 5), (5, 5), (5, 5)])


def test_negative_values():
    assert(fse([-1, 5, 11], 10) == [(-1, 11)])
    assert(fse([-1, -2], -3) == [(-2, -1)])

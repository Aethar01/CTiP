#!/usr/bin/env python3

def get_max(v: list) -> int:
    max = v[0]
    for i in range(1, len(v)):
        if v[i] > max:
            max = v[i]
    return max


def sum_list(v: list) -> int:
    sum = 0
    for i in range(len(v)):
        sum += v[i]
    return sum


def reverse_string(s: str) -> str:
    return s[::-1]


def unique_elements(v: list) -> list:
    return list(set(v))

"""
https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem
"""


def rotLeft(a, d):
    L = len(a)
    new_array = [a[(i + d) % L] for i in range(L)]

    return new_array

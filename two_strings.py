"""
https://www.hackerrank.com/challenges/two-strings/problem
"""


def twoStrings(s1, s2):
    if set(s1).intersection(set(s2)) == set():
        return "NO"
    else:
        return "YES"

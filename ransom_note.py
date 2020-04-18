"""
https://www.hackerrank.com/challenges/ctci-ransom-note/problem
"""


def checkMagazine(magazine, note):
    diff = Counter(note) - Counter(magazine)
    if diff == {}:
        print("Yes")
    else:
        print("No")

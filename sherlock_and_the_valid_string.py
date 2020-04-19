"""
https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=strings
"""


from collections import Counter


def isValid(s):
    s1 = Counter(s)
    values = list(s1.values())
    val_max = max(s1.values())
    val_min = min(s1.values())

    if (
            val_max == val_min or
            (val_max - val_min == 1 and values.count(val_max) == 1) or
            (val_min == 1 and values.count(val_min) == 1)):
        return 'YES'
    else:
        return 'NO'

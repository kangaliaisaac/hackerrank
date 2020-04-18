"""
https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem
"""

from collections import Counter

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    count = 0
    for i in range(1, len(s) + 1):
        an = ["".join(sorted(s[j:j + i])) for j in range(len(s) - i + 1)]
        bn = Counter(an)
        for j in bn:
            count += bn[j] * (bn[j] - 1) / 2

    return int(count)

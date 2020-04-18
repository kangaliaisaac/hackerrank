"""
https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=warmup
"""

from collections import Counter


# Complete the repeatedString function below.
def repeatedString(s, n):
    if all(char == "a" for char in s):
        return n
    else:
        if not n % len(s):
            counter = Counter(s)
            return counter["a"] * (n // len(s))
        else:
            counter1 = Counter(s)
            counter2 = Counter(s[:(n % len(s))])
            count = counter1["a"] * (n // len(s)) + counter2["a"]
            return count

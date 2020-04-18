"""
https://www.hackerrank.com/challenges/alternating-characters/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=strings
"""


# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    count = 0
    L = len(s)
    for i in range(L - 1):
        if s[i + 1] == s[i]:
            i += 1
            count += 1

    return count

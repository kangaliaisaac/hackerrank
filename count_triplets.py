"""
https://www.hackerrank.com/challenges/count-triplets-1/problem
"""


from collections import defaultdict

# Complete the countTriplets function below.
def countTriplets(arr, r):
    v2 = defaultdict(int)
    v3 = defaultdict(int)
    count = 0
    for k in arr:
        count += v3[k]
        v3[k*r] += v2[k]
        v2[k*r] += 1

    return count

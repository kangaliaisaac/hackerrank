"""
https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=warmup
"""


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    count = 0
    idx1 = 0
    last_index = len(c) - 1
    while idx1 < last_index:
        idx2 = idx1 + 1
        idx3 = idx1 + 2
        if idx3 <= last_index:
            if c[idx3] == c[idx1] == 0:
                idx1 = idx3
                count += 1
            else:
                idx1 = idx2
                count += 1
        else:
            idx1 = idx2
            count += 1

    return count

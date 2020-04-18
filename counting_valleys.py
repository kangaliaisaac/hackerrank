"""
https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=warmup
"""


# Complete the countingValleys function below.
def countingValleys(n, s):
    prev_level, curr_level, valley_count = 0, 0, 0

    for c in s:
        if c == "U":
            prev_level, curr_level = curr_level, curr_level + 1
        else:
            prev_level, curr_level = curr_level, curr_level - 1

        if prev_level < 0 and curr_level == 0:
            valley_count += 1

    return valley_count

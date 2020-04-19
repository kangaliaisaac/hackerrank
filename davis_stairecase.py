"""
https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=recursion-backtracking

Hint: Davis has a number of staircases in his house and he likes to climb each staircase 1, 2, or 3 steps at a time
Explanation: https://cs.stackexchange.com/questions/79479/recursion-davis-staircase-understanding
Best solution should take O(n log n) complexity:
Calculations here:
    - https://en.wikipedia.org/wiki/Fibonacci_number#Matrix_form
    - https://www.nayuki.io/page/fast-fibonacci-algorithms
    - https://cs.stackexchange.com/questions/37571/efficient-algorithm-to-compute-the-nth-fibonacci-number

You can optionally use user-defined memoization or functools.lru_cache
    - https://stackoverflow.com/questions/18172257/efficient-calculation-of-fibonacci-series
"""

from functools import lru_cache


@lru_cache(None)
def stepPerms(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    if n > 3:
        return stepPerms(n - 1) + stepPerms(n - 2) + stepPerms(n - 3)


print(stepPerms(32))

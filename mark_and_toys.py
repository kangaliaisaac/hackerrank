"""
https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=strings
"""


def maximumToys(prices, k):
    prices.sort()
    count = 0
    sum_so_far = 0

    for price in prices:
        sum_so_far += price
        count += 1
        if sum_so_far > k:
            break

    return count - 1

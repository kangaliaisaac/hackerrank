"""
https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=warmup
"""


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    freq = {}
    count = 0
    for num in ar:
        freq[str(num)] = 1 + freq.get(str(num), 0)

    for key in freq.keys():
        count += freq[key] // 2

    return count

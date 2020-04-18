"""
https://www.hackerrank.com/challenges/flipping-bits/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=miscellaneous
"""


# Complete the flippingBits function below.
def flippingBits(n):
    n_bit32 = "{0:32b}".format(n)
    lst = list(n_bit32)
    for i in range(len(lst)):
        if lst[i] == " " or lst[i] == "0":
            lst[i] = "1"
        else:
            lst[i] = "0"

    return int("".join(lst), 2)

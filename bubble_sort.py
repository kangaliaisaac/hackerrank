"""
https://www.hackerrank.com/challenges/ctci-bubble-sort/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=sorting
"""


def countSwaps(a):
    L = len(a)
    count = 0
    for i in range(L):
        for j in range(L - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                count += 1

    print("Array is sorted in %d swaps." % count)
    print("First Element: %d" % a[0])
    print("Last Element: %d" % a[-1])

"""
https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=greedy-algorithms
"""


# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    set_arr = set(arr)
    if len(arr) != len(set_arr):
        return 0
    else:
        A = list(set_arr)
        A.sort()
        L = len(A)
        smallest = A[1] - A[0]
        for i in range(1, L - 1, 1):
            j = i + 1
            diff = abs(A[j] - A[i])
            if diff < smallest:
                smallest = diff
            else:
                j += 1
                if j == L:
                    break
            # for j in range(i + 1, L, 1):
            #     diff = abs(A[j] - A[i])
            #     if diff < smallest:
            #         smallest = diff

        return smallest

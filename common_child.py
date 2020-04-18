"""
https://www.hackerrank.com/challenges/common-child/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=strings
"""


# Complete the commonChild function below.
def commonChild(s1, s2):
    # count = 0
    # _temp = 0
    # l1 = s1 if s1[0] == s2[0] else s1 if s1[0] < s2[0] else s2
    # l2 = s2 if s2[0] == s1[0] else s1 if s1[0] > s2[0] else s2
    # for i in range(len(l1)):
    #     for j in range(_temp, len(l2)):
    #         candidate = l1[i]
    #         if l2[j] == candidate:
    #             i += 1
    #             j += 1
    #             count += 1
    #             _temp = j
    #         else:
    #             j += 1
    #     if i == (len(l1) - 1):
    #         break

    # return count
    m, n = len(s1), len(s2)
    prev, cur = [0]*(n+1), [0]*(n+1)
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                cur[j] = 1 + prev[j-1]
            else:
                if cur[j-1] > prev[j]:
                    cur[j] = cur[j-1]
                else:
                    cur[j] = prev[j]
        cur, prev = prev, cur
    return prev[n]

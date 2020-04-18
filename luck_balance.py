"""
https://www.hackerrank.com/challenges/luck-balance/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=greedy-algorithms
"""

from functools import reduce


# Complete the luckBalance function below.
def luckBalance(k, contests):
    # if k == 0:
    #     to_remove = [i[0] for i in contests]
    #     totals_to_remove = reduce(lambda x, y: x + y, to_remove, 0)
    #     # result = totals_to_remove * -1

    #     return totals_to_remove
    # else:
    #     for_1 = []
    #     for_0 = []
    #     L = len(contests)
    #     for i in range(L):
    #         if contests[i][1] == 1:
    #             for_1.append(contests[i])
    #         else:
    #             for_0.append(contests[i])

    #     to_add = []
    #     to_remove = []
    #     for_1.sort()
    #     to_add = for_1[-k:]
    #     to_remove = for_1[: - k]
    #     to_add.extend(for_0)
    #     to_add = [i[0] for i in to_add]
    #     to_remove = [i[0] for i in to_remove]
    #     totals_to_add = reduce(lambda x, y: x + y, to_add, 0)
    #     totals_to_remove = reduce(lambda x, y: x + y, to_remove, 0)
    #     result = totals_to_add - totals_to_remove

    #     return result
    total_luck = 0
    for luck, important in sorted(contests, reverse=True):
        if not important:
            total_luck += luck
        elif k:
            total_luck += luck
            k -= 1
        else:
            total_luck -= luck
    return total_luck

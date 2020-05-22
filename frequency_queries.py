from collections import defaultdict


def freqQuery(A):
    out = []
    freq = defaultdict(int)

    for item in A:
        if item[0] == 1:
            freq[item[1]] += 1
        if item[0] == 2:
            freq[item[1]] -= 1 if freq[item[1]] > 0 else 0
        if item[0] == 3:
            if item[1] in freq.values():
                out.append(1)
            else:
                out.append(0)

        import pdb; pdb.set_trace()

    return out


print(freqQuery([(1,1),(2,2),(3,2),(1,1),(1,1),(2,1),(3,2)]))
# print(freqQuery([(1,5),(1,6),(3,2),(1,10),(1,10),(1,6),(2,5),(3,2)]))
# print(freqQuery([(3, 4), (2, 1003), (1, 16), (3, 1)]))
# print(freqQuery([(1,3),(2,3),(3,2),(1,4),(1,5),(1,5),(1,4),(3,2),(2,4),(3,2)]))

"""
Question: https://www.hackerrank.com/challenges/largest-rectangle/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=stacks-queues

Explanation/Tutorial:
    - https://www.youtube.com/watch?v=RVIh0snn4Qc
    - https://www.youtube.com/watch?v=VNbkzsnllsU
    - https://www.youtube.com/watch?v=ZmnqCZp9bBs
    - https://tech.pic-collage.com/algorithm-largest-area-in-histogram-84cc70500f0c

Runs in O(n) time
"""

class Empty(Exception):
    pass


class ArrayStack:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def peek(self):
        if self.is_empty():
            raise Empty("The stack is empty!")
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty("The stack is empty!")
        return self._data.pop()

    def push(self, val):
        self._data.append(val)


def largestRectangle(h):
    S = ArrayStack()
    max_area = 0
    i = 0
    L = len(h)
    while i < L:
        if S.is_empty() or h[S.peek()] <= h[i]:
            S.push(i)
            i += 1
        else:
            _top = S.pop()
            _width = i if S.is_empty() else (i - S.peek() - 1)
            _area = h[_top] * _width
            if _area > max_area:
                max_area = _area

    while not S.is_empty():
        _top = S.pop()
        _width = i if S.is_empty() else (i - S.peek() - 1)
        _area = h[_top] * _width
        if _area > max_area:
            max_area = _area

    return max_area



print(largestRectangle([11, 11, 10, 10, 10]))

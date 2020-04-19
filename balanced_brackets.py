"""
https://www.hackerrank.com/challenges/balanced-brackets/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=stacks-queues
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

    def pop(self):
        if self.is_empty():
            raise Empty("The stack is empty.")
        return self._data.pop()

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty("The stack is empty.")
        return self._data[-1]


def isBalanced(s):
    lefty = "({["
    righty = ")}]"
    S = ArrayStack()
    for c in s:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return "NO"
            if righty.index(c) != lefty.index(S.pop()):
                return "NO"
    return "YES" if S.is_empty() else "NO"

class Empty(Exception):
    pass


class ArrayStack:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def data(self):
        return self._data

    def pop(self):
        if self.is_empty():
            raise Empty("The stack is empty.")
        return self._data.pop()

    def top(self):
        if self.is_empty():
            raise Empty("The stack is empty.")
        return self._data[-1]

    def push_right(self, e):
        self._data.append(e)

    def push_left(self, e):
        self._data = [e] + self._data


queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())

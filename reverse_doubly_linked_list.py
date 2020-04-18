"""
https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=linked-lists
"""


def reverse(head):
    if head:
        _temp = head
        new_head = head
        while _temp is not None:
            prev = _temp.prev
            _temp.prev = _temp.next
            _temp.next = prev
            new_head = _temp
            _temp = _temp.prev
        return new_head

    return head

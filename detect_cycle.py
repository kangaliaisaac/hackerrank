"""
https://www.hackerrank.com/challenges/ctci-linked-list-cycle/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=linked-lists
"""


def has_cycle(head):
    if (head is None) or (head is not None and head.next is None):
        return False
    else:
        node = head.next
        result = False
        while node:
            next = node.next
            if next is not None and next.next == node:
                result = True
                break
            elif next is None:
                result = False
                break
            else:
                node = next

        return result

"""
https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=linked-lists
"""


def insertNodeAtPosition(head, data, position):
    if position == 0:
        new_node = SinglyLinkedListNode(data)
        new_node.next = head
        head = new_node
        return head
    else:
        new_node = SinglyLinkedListNode(data)
        node = head.next
        while position > 2:
            node = node.next
            if node:
                position -= 1

        old_next = node.next
        node.next = new_node
        new_node.next = old_next

        return head

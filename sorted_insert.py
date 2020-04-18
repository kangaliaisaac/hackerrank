"""
https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=linked-lists
"""


def sortedInsert(head, data):
    new_node = DoublyLinkedListNode(data)
    if data < head.data:
        new_node.next = head
        head.prev = new_node
        head = new_node
    else:
        node = head.next
        while node:
            if node.data < data:
                if node.next is not None:
                    node = node.next
                else:
                    node = node
                    break
            else:
                node = node.prev
                break

        old_next = node.next
        node.next = new_node
        new_node.prev = node
        new_node.next = old_next
        if old_next:
            old_next.prev = new_node

    return head

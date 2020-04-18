"""
https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=trees
"""


def num_children(node):
    count = 0
    if node.left is not None:
        count += 1
    if node.right is not None:
        count += 1

    return count

def children(node):
    if node.left is not None:
        yield node.left
    if node.right is not None:
        yield node.right

def is_leaf(node):
    return num_children(node) == 0

def height(root):
    return 0 if is_leaf(root) else 1 + max(height(p) for p in children(root))

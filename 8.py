# Problem 8 - Ben Stobaugh
#
# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
#
# Given the root to a binary tree, count the number of unival subtrees.
#
# For example, the following tree has 5 unival subtrees:
#
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def num_unival(node, above = None):
    if node is None:
        return 0

    below = set()
    if above is None:
        above = set()


    if node.left is None and node.right is None:
        above.add(node.val)
        return 1

    num = num_unival(node.left, below)
    num += num_unival(node.right, below)

    if len(below) == 1 and node.val in below:
        num += 1

    above.update(below)
    return num

if __name__ == "__main__":
    tree = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
    assert num_unival(tree) == 5, "given"

    tree = Node(1, Node(1, Node(1), Node(1)), Node(1, Node(1), Node(1)))
    assert num_unival(tree) == 7

    tree = Node("a", Node("a"), Node("a", Node("a"), Node("a", None, Node("A"))))
    assert num_unival(tree) == 3

    tree = Node("a", Node("c"), Node("b", Node("b"), Node("b", None, Node("b"))))
    assert num_unival(tree) == 5
# Ben Stobaugh

# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s),
# which deserializes the string back into the tree.
#
# For example, given the following Node class
#
# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# The following test should pass:
#
# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root, curstr=""):
    if root is None:
        return curstr + " NONE"

    curstr += " " + root.val


    curstr = serialize(root.left, curstr)
    curstr = serialize(root.right, curstr)


    return curstr


def deserialize(curstr, curroot=None, left=False):
    first = False

    if curstr is None:
        return None

    curstr = curstr.strip()
    parts = curstr.split(" ", 1)
    this_part = parts[0]
    if len(parts) > 1:
        curstr = parts[1]
    else:
        curstr = None

    if (this_part == "NONE"):
        return curstr

    node = Node(this_part)

    if curroot != None:
        if(left):
            curroot.left = node
            curstr = deserialize(curstr, curroot.left, True)
            curstr = deserialize(curstr, curroot.left, False)
        else:
            curroot.right = node
            curstr = deserialize(curstr, curroot.right, True)
            curstr = deserialize(curstr, curroot.right, False)
    else:
        first = True
        curroot = node
        curstr = deserialize(curstr, curroot, True)
        curstr = deserialize(curstr, curroot, False)


    return curroot if first else curstr


if __name__ == "__main__":
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
    assert deserialize(serialize(node)).right.val == 'right'
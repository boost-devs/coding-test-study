import sys


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def make_tree(root, child):
    if root < child:
        if tree[root].left:
            make_tree(tree[root].left.val, child)
        else:
            tree[root].left = tree[child]
    else:
        if tree[root].right:
            make_tree(tree[root].right.val, child)
        else:
            tree[root].right = tree[child]


def postorder_traverse(node):
    postorder_traverse(node.left)
    postorder_traverse(node.right)
    print(node.val, end="")


tree = {}
root = None
for line in sys.stdin:
    node = int(line.rstrip())
    if not root:
        root = node
        tree[root] = Node(root)
        continue
    tree[node] = Node(node)
    make_tree(root, node)

postorder_traverse(tree[root])

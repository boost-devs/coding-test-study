import sys

input = sys.stdin.readline


class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def preorder_traverse(node):
    print(node.val, end="")
    if node.left:
        preorder_traverse(tree[node.left])
    if node.right:
        preorder_traverse(tree[node.right])


def inorder_traverse(node):
    if node.left:
        inorder_traverse(tree[node.left])
    print(node.val, end="")
    if node.right:
        inorder_traverse(tree[node.right])


def postorder_traverse(node):
    if node.left:
        postorder_traverse(tree[node.left])
    if node.right:
        postorder_traverse(tree[node.right])
    print(node.val, end="")


def has_child(child):
    if child != ".":
        return True
    return False


# 입력
N = int(input())
tree = {}
for _ in range(N):
    val, left, right = input().split()
    left = left if has_child(left) else None
    right = right if has_child(right) else None
    tree[val] = Node(val, left, right)

preorder_traverse(tree["A"])
print()
inorder_traverse(tree["A"])
print()
postorder_traverse(tree["A"])

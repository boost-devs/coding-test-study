###### 1991번: 트리 순회
# https://www.acmicpc.net/problem/1991
# 메모리/시간: 29200KB / 64ms

import sys

input = sys.stdin.readline

N = int(input())

tree = dict()

for _ in range(N):
    node, left, right = input().split()
    tree[node] = [left, right]

def preorder_traversal(node):
    global preorder
    left, right = tree[node]
    preorder.append(node)
    if left != ".":
        preorder_traversal(left)
    if right != ".":
        preorder_traversal(right)

def inorder_traversal(node):
    global inorder
    left, right = tree[node]
    if left != ".":
        inorder_traversal(left)
    inorder.append(node)
    if right != ".":
        inorder_traversal(right)

def postorder_traversal(node):
    global postorder
    left, right = tree[node]
    if left != ".":
        postorder_traversal(left)
    if right != ".":
        postorder_traversal(right)
    postorder.append(node)

preorder = []
inorder = []
postorder = []

preorder_traversal("A")
inorder_traversal("A")
postorder_traversal("A")

print("".join(map(str, preorder)))
print("".join(map(str, inorder)))
print("".join(map(str, postorder)))
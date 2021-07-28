# https://www.acmicpc.net/problem/11659
# 구간 합 구하기 4
# 39776 KB / 2140 ms


import sys


def readline():
    return list(map(int, sys.stdin.readline().split()))


def _init(tree, node, start=None, end=None):
    global arr
    
    if start is None:
        start = 0
    if end is None:
        end = len(arr) - 1
    
    if start == end:
        tree[node] = arr[start]
    else:    
        mid = (start + end) // 2
        tree[node] = (
            _init(tree, node * 2, start, mid)
            + _init(tree, node * 2 + 1, mid + 1, end)
        )
    return tree[node]


def init_tree(arr):
    tree = [0] * (4 * len(arr))
    _init(tree, 1)
    return tree


def sum(node, start, end, i, j):
    global seg_tree

    if i > end or j < start:
        return 0
    
    if i <= start and j >= end:
        return seg_tree[node]
    
    mid = (start + end) // 2
    return (
        sum(node * 2, start, mid, i, j)
        + sum(node * 2 + 1, mid + 1, end, i, j)
    )


n, m = readline()
arr = readline()
l = len(arr)

seg_tree = init_tree(arr)
for _ in range(m):
    i, j = readline()
    print(sum(1, 0, l - 1, i - 1, j - 1))

###### 5639번: 이진 검색 트리
# https://www.acmicpc.net/problem/5639
# 메모리/시간: 38456KB / 4508ms

import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

preorder = []

while True:
    _input = input()
    if _input == "":
        break
    preorder.append(int(_input))

def postorder(start, end):
    if start > end:
        return None
    
    root = preorder[start]
    idx = start + 1
    
    while idx <= end:
        if preorder[idx] > root:
            break
        idx += 1
    
    postorder(start+1, idx-1)
    postorder(idx, end)
    print(root)

postorder(0, len(preorder)-1)
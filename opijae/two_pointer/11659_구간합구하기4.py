import sys
input = sys.stdin.readline

n,m = map(int, input().split())
# arr = [0]
arr = list(map(int, input().split()))
# sum_arr = []
for i in range(n):
    if i ==0:
        sum_arr = [0,arr[0]]
    else:
        sum_arr.append(arr[i] + sum_arr[i])
print(sum_arr)
for _ in range(m):
    s,e = map(int, input().split())
    print(sum_arr[e]-sum_arr[s-1])
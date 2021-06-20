# String
# Problem: 20291
# Memory: 42440KB
# Time: 2440ms

N = int(input())
ans = {}
for i in range(N):
    s = input().split('.')[1]
    if s in ans:
        ans[s] += 1
    else:
        ans[s] = 1

for k, v in sorted(ans.items()):
    print(k + ' ' + str(v))

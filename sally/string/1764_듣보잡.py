# String
# Problem: 1764
# Memory: 35344KB
# Time: 3888ms

L = input()
N = int(L.split(' ')[0])
M = int(L.split(' ')[1])

target = set()
answer = []
for i in range(N):
    s = input()
    target.add(s)

for i in range(M):
    s = input()
    if s in target:
        answer.append(s)


ans = sorted(answer)
print(len(ans))
for i in ans:
    print(i)


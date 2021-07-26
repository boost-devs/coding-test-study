# String
# Problem: 1316
# Memory: 29200KB
# Time: 80ms

N = int(input())
result = 0
for T in range(N):
    s2 = s1 = input()

    s1 += ' '
    cnt1 = 0
    for i in range(len(s1) - 1):
        if s1[i] != s1[i+1]:
            cnt1+=1

    cnt2 = 0
    s2 = ''.join(sorted(s2))
    s2 += ' '
    for i in range(len(s2) - 1):
        if s2[i] != s2[i+1]:
            cnt2+=1

    if cnt1 == cnt2:
        result += 1

print(result)


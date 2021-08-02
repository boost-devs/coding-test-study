import sys
input = sys.stdin.readline

n = int(input())
v =list(map(int, input().split()))
ans, cnt = 0, [0] * 40001

for i in range(n):
    ans += cnt[20000 - v[i]] # i,j,k가 있을때 i+j = -k 가 되야된다는 것을 이용
    for j in range(i):
        cnt[20000 + v[i] + v[j]] += 1 # i + j의 합을 배열 index로 저장
print(ans)
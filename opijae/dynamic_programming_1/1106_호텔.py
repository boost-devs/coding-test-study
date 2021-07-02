import sys
input = sys.stdin.readline
target_num , n = map(int, input().split())

dp=[0]*1000000 # 최소 비용의 dp. dp[1]은 비용 1일때 최대 손님 수
arr=[]
for _ in range(n):
    arr.append(list(map(int, input().split())))
i=1
while(True):
    for cost,customer in arr:
        if cost>i: # cost가 i보다 크면 dp[i-cost]가 음수로 되니 continue
            continue
        temp=dp[i-cost]+customer 
        if temp>dp[i]:
            dp[i]=temp
    if dp[i]>=target_num: # 현재 최소값이 target 수보다 크면 break
        break
    i+=1
print(i)
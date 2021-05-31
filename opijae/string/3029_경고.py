# https://www.acmicpc.net/problem/3029
import sys

input= sys.stdin.readline

start_t=list(map(int,input().split(':')))
end_t=list(map(int,input().split(':')))
start_t=start_t[0]*3600 +start_t[1]*60+start_t[2]  # 전부 초로 바꿈 
end_t=end_t[0]*3600 +end_t[1]*60+end_t[2]
if start_t >=end_t:
    end_t += 24 *3600
period_t=end_t-start_t
h=period_t//3600 # 시는 3600으로 나누고
period_t-=h*3600 
m=period_t//60 # 분은 60으로 나누고
period_t-=m*60
s=period_t # 나머지는 초
print('{0}:{1}:{2}'.format(str(h).zfill(2),str(m).zfill(2),str(s).zfill(2)))

n,k = map(int,input().split())
n = str(n)
lst = list(map(str,input().split()))
lst.sort()
lst.reverse()
lst.append('')

answer = 0

def dfs(x,len_n):
    global answer
    if len_n == len(n):
        if x != '':
            if int(x) <= int(n):
                answer = max(answer,int(x))
    else:
        for i in lst:
            dfs(x+i,len_n+1)
dfs('',0)

print(answer)

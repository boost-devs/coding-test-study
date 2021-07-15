import sys
def solve():
    input = sys.stdin.readline
    arr=[]
    n,m=map(int,input().split())
    for _ in range(n):
        arr.append(list(map(int,input().split())))

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if arr[i][j]>arr[i][k]+arr[k][j]:
                    arr[i][j]=arr[i][k]+arr[k][j]

    for _ in range(m):
        a,b,c=map(int,input().split())
        if arr[a-1][b-1]>c:
            print("Stay here")
        else:
            print("Enjoy other party")

solve()
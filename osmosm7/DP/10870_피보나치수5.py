def DP(x):
    if x == 0:
        return 0
    elif x == 1 :
        return 1
    else:
        return DP(x-1) + DP(x-2)
        
        
if __name__ =='__main__':
    n = int(input())
    answer = DP(n)
    print(answer)
#2748_피보나치수2
import sys
def DP(x,num_list):
    if num_list[x] != -1:
        return num_list[x]
    else:
        num_list[x]  =  DP(x-1,num_list) + DP(x-2,num_list) 
        return num_list[x]
        
        
if __name__ =='__main__':
    n = int(input())
    if n ==1 or n ==2:
        print(1)
        sys.exit()
    elif n == 0:
        print(0)
        sys.exit()
    
    lst = [-1] * (n+1)
    lst[1] = 1
    lst[2] = 1
    answer = DP(n,lst)
    print(answer)
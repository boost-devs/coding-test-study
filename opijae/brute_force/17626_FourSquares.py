import sys
input = sys.stdin.readline
n=int(input())

def is_square(n):
    if n==int(n**0.5)**2:
        return True
    else:
        return False
def is_two(n):
    for i in range(int(n**0.5) ,0,-1):
        if is_square(n-i**2):
            return True
        if i**2<n/2: # n/2 보다 작은것은 볼피요 없다.
            return False
    return False
def is_three(n):
    for i in range(int(n**0.5),0,-1):
        if is_two(n-i**2):
            return True
        if i**2<n/2:
            return False
    return False
if is_square(n): print(1)
elif is_two(n) : print(2)
elif is_three(n) : print(3)
else : print(4)

# print(is_two(12985))
# print(is_three(11339))
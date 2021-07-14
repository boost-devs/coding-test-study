import sys
input = sys.stdin.readline
n=int(input())

def is_square(n):
    """ 제곱수인지 판단
    """
    if n==int(n**0.5)**2: # int로 바꾼후 제곱한 값이 원래값이랑 같으면 제곱수
        return True
    else:
        return False
def is_two(n):
    """ 두 수로 제곱수가 되는지 판단
        n보다 작은 수 중 가장 큰 제곱수 부터 본다.
        n=a**2+b**2 (a>b)
    """
    for i in range(int(n**0.5),0,-1):
        if i**2<n/2:
            return False
        if is_square(n-i**2):
            return True
    return False
def is_three(n):
    """ 세 수로 제곱수가 되는지 판단
        n보다 작은 수 중 가장 큰 제곱수 부터 본다.
        n=a**2+b**2 (a>b) b는 is_two를 만족해여된다.
    """
    for i in range(int(n**0.5),0,-1):
        if i**2<n/2:
            return False
        if is_two(n-i**2):
            return True
    return False
if is_square(n): print(1)
elif is_two(n) : print(2)
elif is_three(n) : print(3)
else : print(4)
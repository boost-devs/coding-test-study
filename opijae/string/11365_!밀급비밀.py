import sys
input=sys.stdin.readline
while True:
    string=input().rstrip()
    if string=='END':
        break
    # 문자열 뒤집기
    print(string[::-1])
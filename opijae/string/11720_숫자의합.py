# https://www.acmicpc.net/problem/11720
import sys

input=sys.stdin.readline

a=input()
print(sum(map(int,list(input().rstrip())))) # 들어온 것들 list -> int형으로 -> sum
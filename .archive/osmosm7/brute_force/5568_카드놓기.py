from itertools import permutations

n = int(input())
k = int(input())

lst = [input() for _ in range(n)]

hubo = set(''.join(num) for num in list(permutations(lst,k)))

print(len(hubo))
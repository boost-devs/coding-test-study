# https://www.acmicpc.net/problem/3151
# 합이 0
#


N = int(input())
arr = [int(a) for a in input().split()]

arr.sort()
print(arr)
count = 0
for t in range(N - 3):
    l, r = N - 2, N - 1
    while l < N - 1:
        _sum = arr[t] + arr[l] + arr[r]
        if _sum < 0:
            l += 1
        elif _sum > 0:
            r -= 1
        else:
            if arr[l] == arr[r]:
                count += r - l
                break
            else:
                while arr[l + 1] == arr[l]:
                    count += 1
                    l += 1
                else:
                    l += 1
                while arr[r - 1] == arr[r]:
                    count += 1
                    r -= 1
                else:
                    r -= 1
            print(arr[t], arr[l], arr[r])

print(count)

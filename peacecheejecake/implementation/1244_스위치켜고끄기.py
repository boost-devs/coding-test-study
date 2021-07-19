# https://www.acmicpc.net/problem/1244
# 스위치 켜고 끄기
# 29200 KB / 80 ms


def switch(type, given, status):
    given = int(given)
    if type == '1':
        for i in range(given - 1, len(status), given):
            status[i] = 1 - status[i]
    else:
        status[given - 1] = 1 - status[given - 1]
        for i in range(1, min(given, len(status) - given + 1)):
            if status[given - 1 - i] != status[given - 1 + i]:
                break
            status[given - 1 - i] = 1 - status[given - 1 - i]
            status[given - 1 + i] = status[given - 1 - i]


n = int(input())
status = [int(s) for s in input().split()]
num_students = int(input())
for _ in range(num_students):
    switch(*input().split(), status)

for i in range(0, len(status), 20):
    print(' '.join(str(s) for s in status[i:i + 20]))

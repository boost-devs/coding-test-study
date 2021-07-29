# https://www.acmicpc.net/problem/21921
# 블로그
# 58340 KB / 208 ms


N, X = map(int, input().split())
visits = [int(x) for x in input().split()]

_psum = sum(visits[:X])
max_visit = _psum
num_repeat = 1
for i in range(N - X):
    _psum = _psum - visits[i] + visits[i + X]
    if _psum > max_visit:
        max_visit = _psum
        num_repeat = 1
    elif _psum == max_visit:
        num_repeat += 1

if max_visit == 0:
    print("SAD")
else:
    print(f"{max_visit}\n{num_repeat}")

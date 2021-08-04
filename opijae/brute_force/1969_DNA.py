import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [[0,0,0,0] for _ in range(m)]
# DNA -> num
char_dict = {
    'A': 0,
    'C': 1,
    'G': 2,
    'T': 3
}
# num to DNA
char_list = ['A', 'C', 'G', 'T']


def _max(arr):
    """ 배열합 -최대값, 최대값의 index return
    """
    _sum, _max_num, _max_index = 0, 0, 0
    for i in range(4):
        if arr[i] > _max_num:
            _max_num = arr[i]
            _max_index = i
        _sum += arr[i]
    return _sum - _max_num, _max_index

for _ in range(n):
    _input = input().rstrip()
    for i in range(m):
        arr[i][char_dict[_input[i]]] += 1

hamming_dis = 0
result =""
for i in range(m):
    _hamming, _max_index, = _max(arr[i])
    hamming_dis += _hamming
    result+=char_list[_max_index]
print(result)
print(hamming_dis)

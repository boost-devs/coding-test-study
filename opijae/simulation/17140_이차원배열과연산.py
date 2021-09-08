import sys
from collections import defaultdict
input = sys.stdin.readline

r,c,k = map(int, input().split())
# arr[r][c] == k인지 확인
def check(arr ,r , c):
    _row_num = len(arr)
    _col_num = len(arr[0])
    if r > _row_num or c > _col_num: # arr이 바뀌면서 idnex 에러 날 수 있음
        return True
    if arr[r-1][c-1] == k:
        return False
    else:
        return True
arr = []
for _ in range(3):
    arr.append(list(map(int, input().split())))
cnt = 0
while check(arr,r,c):
    _row_num = len(arr)
    _col_num = len(arr[0])
    _new_arr = [] # 새로운 배열
    _max_len = 0
    if _row_num> 100: # 행이 100보다 많은 경우
        arr = arr[:100]
    if _col_num> 100: # 열이 100보다 많은 경우
        temp = []
        for row in arr:
            temp.append(row[:100])
        arr = temp[:] # arr 값 업데이트
    if _row_num >= _col_num: # 행이 길때
        for row in arr:
            temp = []
            count_list = defaultdict(int)
            for num in row:
                if num: # 0빼고 카운트
                    count_list[num] += 1
            for v in sorted(count_list.items(),key = lambda x:(x[1],x[0])): # 문제에서 주어진대로 정혛
                temp.append(v[0])
                temp.append(v[1])
            _new_arr.append(temp)
            _max_len = max(_max_len,len(temp)) # 최대 길이 구하기
        for i in range(len(_new_arr)): # 최대 길이 만큼 패딩
            while len(_new_arr[i]) < _max_len:
                _new_arr[i].append(0)
        arr = _new_arr[:] # arr 값 업데이트
    else:
        for col_idx in range(_col_num):
            temp = []
            count_list = defaultdict(int)
            for row in arr:
                if row[col_idx]:
                    count_list[row[col_idx]] += 1
            for v in sorted(count_list.items(),key = lambda x:(x[1],x[0])):
                temp.append(v[0])
                temp.append(v[1])
            _new_arr.append(temp)
            _max_len = max(_max_len,len(temp))
        for i in range(len(_new_arr)):
            while len(_new_arr[i]) < _max_len:
                _new_arr[i].append(0)
        # 행으로 업데이트 된것을 열로 바꿔야됨
        temp = [[0]*_col_num for _ in range(_max_len)]
        for i in range(_col_num):
            for j in range(_max_len):
                temp[j][i] = _new_arr[i][j]
        arr = temp[:]
    cnt +=1
    if cnt >100:
        print(-1)
        sys.exit()
print(cnt)
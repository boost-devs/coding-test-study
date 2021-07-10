# https://www.acmicpc.net/problem/21317
# 징검다리 건너기
# 29200 KB / 80 ms


def fill_table(table, start):
    global stones
    for i in range(start + 2, n):
        table.append(min(
            table[i - start - 2] + stones[i - 2][1],
            table[i - start - 1] + stones[i - 1][0],
        ))
    return table


n = int(input())

if n == 1:
    print(0)
    exit()
else:
    stones = []
    for _ in range(n - 1):
        stones.append(
            tuple(int(x) for x in input().split())
        )
    k = int(input())

    table = fill_table([0, stones[0][0]], 0)
    sup_cands = []
    for i in range(3, n):
        eng_w_sup = table[i - 3] + k
        if eng_w_sup < table[i]:
            temp_table = fill_table([table[i - 1], eng_w_sup], i - 1)
            sup_cands.append(temp_table[-1])
    
    if sup_cands:
        print(min(sup_cands))
    else:
        print(table[-1])

# String
# Problem: 20437
# Memory: 29200KB
# Time: 528ms

T = int(input())
alphabet = "qwertyuiopasdfghjklzxcvbnm"

for t in range(T):
    W = input()
    K = int(input())

    min_len = 10001
    max_len = 0
    flag = False
    for a in alphabet:
        if a in W:
            if len(W.split(a)) > K:
                flag = True
                pos = -1
                target = []
                while True:
                    pos = W.find(a, pos + 1)
                    if pos == -1:
                        break
                    target.append(pos)
                for i in range(0, len(target)-K+1):
                    x = (target[i+K-1] - target[i])
                    max_len = max(max_len, x)
                    min_len = min(min_len, x)

    if flag == True:
        print(str(min_len+1) + ' ' + str(max_len+1))
    else: print("-1")




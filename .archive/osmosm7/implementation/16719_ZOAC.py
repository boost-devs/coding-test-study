def dfs(word,last_idx):
    global answer    
    if len(word) == 0:
        return
    else: 
        min_idx = word.index(min(word))
        now_cha = word.pop(min_idx)
        answer.append([now_cha, min_idx+last_idx+1])
        answer.sort(key = lambda x: x[1])
        for j in answer:
            print(j[0],end = '')
        print('')
        dfs(word[min_idx:],min_idx+last_idx)
        dfs(word[:min_idx],last_idx)

answer = []
zoac = list(input())
dfs(zoac,-1)
#STARTLINK
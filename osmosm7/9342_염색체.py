# a,b,c,d,e,f 중 0개 또는 1개로 시작해야함
# a가 하나 또는 그 이상,
#f가 하나 또는 그 이상
#c가 하나 또는 그 이상
# a,b,c,d,f,중 0개 또는 1개, 다음은 없어야함
def is_dna(x):
    alp = ['A','B','C','D','E','F']
    test = [alp,'A','F','C',alp]
    
    # alp 외 문자 있으면 False
    if len(set(list(x)) - set(alp)) !=0:
        return print('Good')
    
    #중복 제거
    if x[0] =='A':
        new_dna = 'AA'
    else:
        new_dna = x[0]
    now = x[0]
    for d in range(1,len(x)):
        if x[d] == now:
            continue
        else:
            new_dna += x[d]
            now = x[d]
            
    #AFC순으로 나왔는지 확인
    if new_dna[1:4] != 'AFC':
        return print('Good')
    #AFC 끝나고 alp 안의 1개 or 없는지 확인
    if new_dna[4:] in alp or len(new_dna[4:]) == 0:
        return print('Infected!')
    return print('Good')

if __name__ =='__miain':
    lst = []
    for i in range(int(input())):
        is_dna(input())

        
    
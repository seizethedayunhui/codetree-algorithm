N, M = map(int, input().split())

couples = list()
for _ in range(M) :
    couple = list(map(int, input().split()))
    couple.sort()
    couples.append(couple)

max_cnt = float('-inf')

for i in range(M) :
    couple_cnt = 0
    for j in range(M) :
        
        flag = True
        
        for elem1, elem2 in zip(couples[i], couples[j]) :
            if elem1 != elem2 :
                flag = False
                break
        
        if flag :
            couple_cnt += 1

    max_cnt = max(max_cnt, couple_cnt)

print(max_cnt)
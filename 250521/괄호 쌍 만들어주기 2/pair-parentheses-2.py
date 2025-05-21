A = input()

A_list = list()

for elem in A :
    A_list.append(elem)


cnt = 0

for i in range(len(A)) :
    for j in range(i+1, len(A)) :
        for k in range(j+1, len(A)) :
            for l in range(k+1, len(A)) :

                if abs(i-j) == 1  and abs(k-l) == 1 :
                    if A_list[i] == "(" and A_list[j] == "(" and A_list[k] == ")" and A_list[l] == ")" :
                        cnt += 1


print(cnt)
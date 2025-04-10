A = input()
B = input()
len_A = len(A)
len_B = len(B)

cnt = 0
for i in range(len_A - len_B + 1) :
    flag = True
    for j in range(len_B) :
        if A[i+j] != B[j] :
            flag = False
            break
    if flag :
        cnt += 1
print(cnt)
A = input()

encoding_A = str()

for i in range(len(A)) :
    if not i :
        cnt = 1
        current_elem = A[i]
    else :
        if A[i] == A[i-1] :
            cnt +=1
        else :
            encoding_A += current_elem + str(cnt)
            current_elem = A[i]
            cnt = 1
    if i == len(A) - 1 :
        encoding_A += current_elem + str(cnt)

print(len(encoding_A))       
print(encoding_A)

A, B = map(int, input().split())

cnt_sum = 0

if A > B :
    for i in range(B, A+1) :

        if i % 5 == 0 :
            cnt_sum += i
else :
    for j in range(A, B+1) :

        if j % 5 == 0 :
            cnt_sum += j
    
print(cnt_sum)
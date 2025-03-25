A, B = map(int, input().split())

cnt_sum = 0

for i in range(A, B+1) :

    if ( i % 6 == 0 ) and ( i % 8 ) :
        cnt_sum += i

print(cnt_sum)
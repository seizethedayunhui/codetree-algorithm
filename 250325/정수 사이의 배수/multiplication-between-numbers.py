A, B = map(int, input().split())

cnt = 0
cnt_sum = 0

for i in range(A, B+1) :

    if ( i % 5 == 0 ) or ( i % 7 == 0 ) :
        cnt += 1
        cnt_sum += i

ans = float(cnt_sum / cnt)

print(f"{cnt_sum} {ans:.1f}")
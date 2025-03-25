N_list = [ int(input()) for _ in range(10) ]

cnt = 0
cnt_sum = 0

for number in N_list :

    if number >= 0 and number <= 200 :

        cnt += 1
        cnt_sum += number

ans = ( cnt_sum / cnt )

print(f"{cnt_sum} {ans:.1f}")
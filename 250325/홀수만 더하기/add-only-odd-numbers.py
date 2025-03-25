N = int(input())

N_list = [ int(input()) for _ in range(N) ]

cnt_sum = 0

for number in N_list :

    if ( number % 2 ) and ( number % 3 ==0 ) :
        cnt_sum += number

print(cnt_sum)
N = int(input())

cnt_sum = 0

for i in range( 1, 101 ) :
    
    cnt_sum += i

    if cnt_sum >= N :
        print(i)
        break
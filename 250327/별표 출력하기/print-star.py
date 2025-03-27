N = int(input())

loop_len = N + ( N - 1 )

for i in range(loop_len) :
    if i >= N :
        for k in range( loop_len - i ) :
            print("*", end=" ")
    else :
        for j in range(i + 1) :
            print("*", end= " ")
    print()
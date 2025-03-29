N = int(input())

loop_len = 2 * N + 1

for i in range(1, loop_len + 1) :
    if ( i % 2 ) :
        for _ in range(loop_len) :
            print("*", end=" ")
        print()
    else :
        for j in range (1, loop_len + 1) :
            if ( j % 2 ) :
                print("*", end=" ")
            else :
                print(" ", end=" ")
        print()
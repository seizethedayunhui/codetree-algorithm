N = int(input())

max_len = 2 * N - 1
for i in range(N, 0, -1) :
    current_len = max_len - ( 2*i - 1 )
    blank_len = int(current_len // 2)

    for blank in range(blank_len):
        print(" ", end=" ")

    for j in range( 2*i - 1 ) :
        print("*", end=" ")

    for blank in range(blank_len):
        print(" ", end=" ")

    print()




        
    
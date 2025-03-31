A, B = map(int, input().split())

for i in [ 2, 4, 6, 8 ] :
    for j in range(B, A-1, -1) :
        print(f"{j} * {i} = {j*i}", end="")

        if j > A :
            print(" /", end=" ")
    print()
N = int(input())

for i in range(N) :
    for _ in range(i) :
        print(" ", end=" ")
    for j in range(N-i, 0, -1) :
        print(j, end=" ")
    print()
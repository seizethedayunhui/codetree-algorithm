N = int(input())

for i in range(N) :

    if i == 0 :
        for _ in range(N) :
            print("*", end=" ")
    else :
        for j in range(N) :
            
            if j < i or j == N - 1 :
                print("*", end=" ")
            else :
                print(" ", end=" ")
    print()
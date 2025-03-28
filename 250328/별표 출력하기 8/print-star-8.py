N = int(input())

for i in range(1, N+1) :
    if i % 2 :
        print("*", end="")
    else :
        for _ in range(i):
            print("*", end=" ")
    print()
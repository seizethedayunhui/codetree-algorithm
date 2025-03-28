N = int(input())

odd = N
even = 1

for i in range(1, 2*N+1):
    if i % 2 :
        for _ in range(odd) :
            print("*", end=" ")
        odd -= 1
    else :
        for _ in range(even):
            print("*", end=" ")
        even += 1
    print()
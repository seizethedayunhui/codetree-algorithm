N = int(input())

for i in range(N) :
    for j in range(N, 0, -1) :
        num = (i+1) * j
        print(num, end=" ")
    print()
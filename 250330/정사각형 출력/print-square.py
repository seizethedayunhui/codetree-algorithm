N = int(input())

for i in range(N) :
    num = N *(i+1) -(N-1)
    for _ in range(N) :
        print(num, end= " ")
        num += 1
    print()
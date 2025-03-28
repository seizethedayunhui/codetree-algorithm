N = int(input())

odd = 1
even = N
for i in range(1, 2*N+1) :
        if i % 2 :
            for _ in range(odd):
                print("*", end=" ")
            odd += 1
        else :
            for _ in range(even):
                print("*", end=" ")
            even -= 1
        print()



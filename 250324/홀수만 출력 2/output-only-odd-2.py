B, A = map(int, input().split())

for i in range(B, A-1, -1) :

    if i % 2 :
        print(i, end=" ")
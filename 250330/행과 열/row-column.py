A, B = map(int, input().split())

for i in range(A) :
    for j in range(B) :
        ans = (i+1) * (j+1)
        print(ans, end=" ")
    print()
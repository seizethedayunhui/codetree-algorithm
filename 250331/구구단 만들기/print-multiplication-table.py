A, B = map(int, input().split())

# 행의 개수
for i in range(9) :
    for j in range(B, A-1, -2) :
        print(f"{j} * {i+1} = {j*(i+1)}", end="")

        if j > A :
            print(" /", end=" ")
    print()
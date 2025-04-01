N = int(input())

for i in range(N) :
    for j in range(N-i) :
        print(f"{i+1} * {j+1} = {(i+1)*(j+1)}", end="")
        if j == (N-i) -1 :
            print()
        else :
            print(" / ", end="")

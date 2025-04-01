n = int(input())

for i in range(n) :
    for j in range(n) :
        if ((i+1)+(j+1)) % 4 == 0 :
            print(f"({i+1}, {j+1})")
        else :
            print(f"({i+1}, {j+1})", end=" ")
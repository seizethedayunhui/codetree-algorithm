n = int(input())

for k in range(n) :
    if k % 2 :
        for i in range(n) :
            print( n - i, end="")
        print()
    else :
        for j in range(n) :
            print( j+1, end="")
        print()
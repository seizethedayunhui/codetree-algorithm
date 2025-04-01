N = int(input())

char = 65
for i in range(N) :
    for k in range(i) :
        print(" ", end=" ")
    
    for j in range(N-i) :
        print(chr(char), end=" ")
        if chr(char) == 'Z' :
            char = 65
        else :
            char += 1
    print()
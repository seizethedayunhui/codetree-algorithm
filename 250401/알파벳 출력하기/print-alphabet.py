N = int(input())

char = 65

for i in range(N) :
    for j in range(i+1) :
        if char >= 91 :
            char = 65
        print(chr(char), end="")
        char += 1
    print()
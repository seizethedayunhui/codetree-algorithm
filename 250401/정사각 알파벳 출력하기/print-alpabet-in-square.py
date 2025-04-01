n = int(input())

char = 65
for i in range(n) :
    for j in range(n) :
        print(chr(char), end="")
        char += 1
    print()
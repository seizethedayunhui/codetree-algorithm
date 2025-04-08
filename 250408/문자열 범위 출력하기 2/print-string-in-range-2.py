string = input()
n = int(input())

if n > len(string) :
    for i in range(len(string)-1, -1, -1) :
        print(string[i], end="")
else :
    for i in range(n) :
        print(string[-(i+1)], end="")
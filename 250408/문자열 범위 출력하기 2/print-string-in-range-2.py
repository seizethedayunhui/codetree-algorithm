string = input()
n = int(input())

if n > len(string) :
    print( string[-1:] )
else :
    for i in range(n) :
        print(string[-(i+1)], end="")
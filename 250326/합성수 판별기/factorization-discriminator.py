n = int(input())

flag = 0

for i in range(2, n) :

    if ( n % i == 0 ):
        flag = 1
        break

if flag :
    print("C")
else :
    print("N")
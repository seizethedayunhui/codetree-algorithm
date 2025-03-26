A, B = map(int, input().split())

flag = 0

for i in range(A, B+1) :

    if ( 1920 % i ==0 ) and ( 2880 % i == 0 ) :
        flag = 1
        break

if flag :
    print(1)
else :
    print(0)
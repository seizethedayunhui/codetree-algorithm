N = int(input())

satisfied = True

for i in range(2, N) :

    if ( N % i == 0 ) :
        satisfied = False
        break

if satisfied :
    print("P")
else :
    print("C")
N = int(input())

cnt = 0

i = 1
while cnt != 2 :

    if ( i * N ) % 5 == 0 :
        cnt += 1
    print( i*N, end=" ")
    i += 1


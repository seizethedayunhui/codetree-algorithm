N, B = map(int, input().split())

B_N = str()

while True :

    if N <= 0 :
        break

    B_N = str(( N % B )) + B_N
    N //= B

if B_N :
    print(B_N)
else :
    print(N)
    
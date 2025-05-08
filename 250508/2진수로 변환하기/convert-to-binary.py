N = int(input())

bit_N = str()

while True :

    if N <= 0 :
        break

    else :
        bit_N = str(N % 2) + bit_N
        N //= 2

print(bit_N)


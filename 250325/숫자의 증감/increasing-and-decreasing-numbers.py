C, N = map(str, input().split())

N = int(N)

if C == 'A':
    for i in range(1, N+1) :
        print(i, end=" ")
elif C == 'D' :
    for i in range( N, 0, -1):
        print(i, end=" ")
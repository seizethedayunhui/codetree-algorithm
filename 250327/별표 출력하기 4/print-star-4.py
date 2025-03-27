N = int(input())

loop_len = 2 * N - 1

for i in range(N, 0, -1) :
    for j in range(i):
        print("*", end=" ")
    print()
for i in range(1, N):
    for j in range( i +1 ) :
        print("*", end=" ")
    print()
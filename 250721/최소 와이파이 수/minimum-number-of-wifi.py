n, m = map(int, input().split())

arr = list(map(int, input().split()))

start_point = 0

for i in range(1, n + 1) :

    if ( (m * 2 + 1) * i >= n ) :
        ans = i
        break

print(ans)

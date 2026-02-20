N = int(input())
points = [ list(map(int, input().split())) for _ in range(N) ]

dp = [ -1 for _ in range(1, 10001) ]

cnt = N

for point in points:
    x1 = point[0]
    x2 = point[1]

    l = abs(x2-x1+1)
    min_l = l

    for i in range(x1, x2+1):

        if dp[i] > 0:
            min_l = min(dp[i], l)
            dp[i] = min_l
        else:
            dp[i] = l

    if min_l < l:
        cnt -= 1
        for j in range(x1, x1+1):
            if dp[j] != min_l:
                dp[i] = -1

# for idx in range(1, 100):
#     print(dp[idx], end=" ")

print(cnt)

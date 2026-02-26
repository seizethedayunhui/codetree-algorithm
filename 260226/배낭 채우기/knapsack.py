N, M = map(int, input().split())

weight = [ 0 ] * N
value = [ 0 ] * N

for i in range(N):
    w, v = map(int, input().split())

    weight[i] = w
    value[i] = v

MIN_VALUE = float('-inf')

dp = [MIN_VALUE] * (M+1)

dp[0] = 0

for i in range(N):
    for j in range(M, -1,-1):
            
        if j >= weight[i]:

            #print(dp)

            if dp[j-weight[i]] == MIN_VALUE:
                continue

            dp[j] = max(dp[j], dp[j-weight[i]] + value[i])

ans = float('-inf')

for i in range(M+1):
    ans = max(ans, dp[i])

print(ans)
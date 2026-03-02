N, M = map(int, input().split())
weights = list()
values = list()

for i in range(N):
    weight, value =  map(int, input().split())
    weights.append(weight)
    values.append(value)

dp = [0] * (M+1)

for m in range(1, M+1):
    for i in range(N):
        if m >= weights[i]:
            dp[m] = max(dp[m], dp[m-weights[i]] + values[i])

ans = dp[M]
print(ans)
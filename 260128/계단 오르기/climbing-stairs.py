N = int(input())

dp = [-1] * (N+1)

def step(n):

    if dp[n] != -1:
        return dp[n]
    
    elif n <= 1:
        if n == 0:
            dp[n] = 1
        else:
            dp[n] = 0
    
    else:
        dp[n] = step(n-2) + step(n-3)
    
    return dp[n]

ans = step(N) % 10007
print(ans)
    
    

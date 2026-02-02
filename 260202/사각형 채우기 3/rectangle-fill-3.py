import sys

def solve():
    n = int(sys.stdin.readline())
    MOD = 1000000007
    
    if n == 0:
        print(1)
        return
    if n == 1:
        print(2)
        return
    if n == 2:
        print(7)
        return

    # dp 테이블 초기화
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 2
    dp[2] = 7

    # 점화식 적용: dp[i] = 3 * dp[i-1] + dp[i-2] - dp[i-3]
    for i in range(3, n + 1):
        dp[i] = (3 * dp[i-1] + dp[i-2] - dp[i-3]) % MOD
        
    print(dp[n])

solve()
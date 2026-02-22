N = int(input())

works = [ list(map(int, input().split())) for _ in range(N)]

dp = [0 for _ in range(N)]

dp[0] = works[0][-1]

def check(s1, e1, s2, e2):
    return (s2 <= s1 <= e2)

for i in range(1, N):

    s1, e1, p1 = works[i]
    dp[i] = p1

    for j in range(i):

        s2, e2, p2 = works[j]

        if check(s1, e1, s2, e2):
            dp[i] = max(dp[j], dp[i])
        else:
            dp[i] = max(dp[j] + p1, dp[i])

    #     print(i, j)
    #     for k in range(N):
    #         print(dp[k], end=" ")
    #     print()
    # print()


ans = dp[N-1]
print(ans)

        


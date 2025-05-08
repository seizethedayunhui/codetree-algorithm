N = list(input())

ans = 0

for i in range(len(N)):
    ans += int(N[len(N)-(i+1)]) * (2 ** i)

print(ans)

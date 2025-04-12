n, A = input().split()
n = int(n)

cnt = 0
for _ in range(n) :
    if input() == A :
        cnt += 1
print(cnt)
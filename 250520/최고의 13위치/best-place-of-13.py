N = int(input())

mat = list()
for _ in range(N) :
    row = list(map(int, input().split()))
    mat.append(row)

max_coin = float('-inf')

for i in range(N) :
    for j in range(N-2):
        max_coin = max(max_coin, mat[i][j] + mat[i][j+1] + mat[i][j+2] )

print(max_coin)
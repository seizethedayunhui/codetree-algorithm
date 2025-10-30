N = int(input())

mat = list()
for _ in range(N) :
    arr = list(map(int, input().split()))
    mat.append(arr)

max_coins = float('-inf')
for i in range(N-2) :
    for j in range(N-2) :
        current_coins = 0
        for k in range(i, i+3) :
            for l in range(j, j+3) :
                current_coins += mat[k][l]
        max_coins = max(max_coins, current_coins)
        
print(max_coins)


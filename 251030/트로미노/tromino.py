N, M = map(int, input().split())

mat = list()
for _ in range(N) :
    row = list(map(int, input().split()))
    mat.append(row)

maxSum = float('-inf')

# 3 * 1
for i in range(N-2) :
    for j in range(M) :
        currentSum = 0
        for k in range(3) :
            currentSum += mat[i+k][j]
        maxSum = max(maxSum, currentSum)

# 1 * 3
for i in range(M-2) :
    for j in range(N) :
        currentSum = 0
        for k in range(3) :
            currentSum += mat[j][i+k]
        maxSum = max(maxSum, currentSum) 

dx = [ [ 0, 1, 1], [ 0, 0, 1], [ 0, 0, 1], [ 0, 1, 1] ]
dy = [ [ 0, 0, 1], [ 0, 1, 0], [ 0, 1, 1], [ 1, 1, 0] ]


# 계단 모양
for i in range(N-1):
    for j in range(M-1):   
        # 하나의 지점에 도착
        # 4가지 경우의 수
        for k in range(4):
            currentSum = 0
            for l in range(3):
                currentSum += mat[i + dx[k][l]][j + dy[k][l]]
            maxSum = max(maxSum, currentSum)
            # print(currentSum)

print(maxSum)


        
        

       

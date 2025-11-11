N = int(input())

mat = [ list(map(int, input().split())) for _ in range(N) ]

def in_range(x, y) :
    return 0 <= x < N and 0 <= y < N

dx = [ 0, 1, 0, -1 ]
dy = [ 1, 0, -1, 0 ]

max_cnt = float('-inf')

# 모든 point 기준 탐색
for x in range(N) :
    for y in range(N) :

        temp = [ [ element for element in row ] for row in mat ]

        bomb_range = mat[x][y]-1
        temp[x][y] = 0

        # 폭탄 터지리
        for i in range(4) :
            nx, ny = x, y
            for _ in range(bomb_range) :
                nx += dx[i]
                ny += dy[i]

                if in_range(nx, ny) :
                    temp[nx][ny] = 0

        # 중력 작용
        for col in range(N) :
            for row in range(N-1, -1, -1) :

                if not temp[row][col] :
                    for row2 in range(row-1, -1, -1) :
                        if temp[row2][col] :
                            temp[row][col] = temp[row2][col]
                            temp[row2][col] = 0
                            break

        # for j in range(N) :
        #     for k in range(N) :
        #         print(temp[j][k], end=" ")
        #     print()
        # print()
        
        # 상하좌우 쌍 개수 cnt
        cnt = 0
        for element1 in range(N-1) :
            for element2 in range(N) :

                if temp[element1][element2] :
                    if temp[element1+1][element2] == temp[element1][element2]:
                        cnt += 1
                
                if temp[element2][element1] :
                    if temp[element2][element1] == temp[element2][element1+1]:
                        cnt += 1
                    
        max_cnt = max(max_cnt, cnt)

print(max_cnt)
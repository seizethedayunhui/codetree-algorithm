N = int(input())
mat = list()

# 격자 생성
for _ in range(N) :
    row = list(map(int, input().split()))
    mat.append(row)

max_sum = float('-inf') # 최대 합 저장하는 변수

# 범위 확인해주는 함수
def in_range(x, y, N) :
    return ( 0 <= x < N ) and ( 0 <= y < N )

# 1번 (-1, +1) / 2번 (-1, -1) / 3번 (+1, -1) / 4번 (+1, +1)
# 방향별 인덱스
dx = [-1, -1, 1, 1]
dy = [ 1, -1, -1, 1]

for x in range(N) :
    for y in range(N) :
        
        # 1 & 3번이 갈 수 있는 범위 
        range1 = min(abs(x), abs(N-y-1))

        # 갈수 있는 범위 별로 합 구하기
        for r1 in range(range1) :

            # 2~4번이 갈수 있는 범위를 알아내기 위해 nx, ny 구해서 범위 체크
            nx = x + dx[0] * (r1+1)
            ny = y + dy[0] * (r1+1)

            # 2 & 4번이 갈 수 있는 범위 구하기
            range2 = min(abs(nx), abs(ny))

            # print(f"(x, y) = {nx+1}, {ny+1} : {range2}")
            for r2 in range(range2) :
                
                cx, cy = x, y
                current_sum = 0

                for i in range(4) :
                    if not i % 2 :
                        for _ in range(r1 + 1) :
                            current_sum += mat[cx][cy]
                            cx += dx[i]
                            cy += dy[i]
                    else :
                        for _ in range(r2 + 1) :
                            current_sum += mat[cx][cy]
                            cx += dx[i]
                            cy += dy[i]                           
            
                max_sum = max(max_sum, current_sum)

print(max_sum)




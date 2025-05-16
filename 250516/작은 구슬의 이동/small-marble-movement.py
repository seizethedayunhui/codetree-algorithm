N, T = map(int, input().split())

R, C, D = input().split()

R = int(R)
C = int(C)

# 범위 체킹
def in_range(x, y, N) :
    return (0 <= x < N) and (0<= y < N)

# 입력 받은 방향을 인덱스로 변환
direc_to_idx = {"R" : 0, "D" : 1, "L" : 2, "U" : 3}
dx = [ 0, 1, 0, -1]
dy = [ 1, 0, -1, 0]

x = R - 1
y = C - 1
dir_num = direc_to_idx[D]

# 범위 결정
for _ in range(T) :

    # 다음의 x, y 위치 결정
    nx = x + dx[dir_num]
    ny = y + dy[dir_num]

    # 범위를 벗어난 경우, 밤향 조절
    if not in_range(nx, ny, N) :
        dir_num = ( dir_num + 1 ) % 3
    else :
        x += dx[dir_num]
        y += dy[dir_num]

print(x+1, y+1)
    



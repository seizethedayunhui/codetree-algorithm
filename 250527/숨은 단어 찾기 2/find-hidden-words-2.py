N, M = map(int, input().split())

char_list = list()

for _ in range(N):
    char_list.append(list(input()))


# 범위 안에 있는지 확인하는 함수
def in_range(x, y, N, M) :
    return ( 0 <= x < N ) and ( 0 <= y < M )

string = "LEE"

# 동(가로), 남(세로), 서(가로), 북(세로), 대각오른쪽아래, 대각오른쪽위로, 대각 왼쪽 위로, 대각 왼쪽 아래로
dx = [ 0, 1, 0, -1, 1, -1, -1, 1]
dy = [ 1, 0, -1, 0, 1, 1, -1, -1]



cnt = 0

for x in range(N) :
    for y in range(M) :

        # 가로 세로 모두 확인
        for k in range(8) :
            new_string = char_list[x][y]
            for l in range(2) :

                nx = x + (l+1)*dx[k]
                ny = y + (l+1)*dy[k]

                if in_range(nx, ny, N, M) :
                    new_string += char_list[nx][ny]
                else :
                    break
            # 같으면 cnt ++
            if new_string == string :
                cnt += 1

                
print(cnt)
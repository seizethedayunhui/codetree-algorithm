N = int(input())

mat = list()

for _ in range(N) :

    input_to_list = list()

    for elem in input():
        input_to_list.append(elem)

    mat.append(input_to_list)

dx = [ 0, 1, 0, -1 ]
dy = [ 1, 0, -1, 0 ]

"""
 시작 위치에 따라서 방향이 다름
"""
K = int(input())

if K <= N :
    direc_num = 1
    x = 0
    y = ( K - 1 ) % N
elif K <= 2 * N :
    direc_num = 2
    x = ( K - 1 ) % N 
    y = N - 1
elif K <= 3 * N :
    direc_num = 3
    x = N - 1
    y = 3 * N - K
else :
    direc_num = 0
    x = 4 * n - K
    y = 0

# 범위 확인 함수
def in_range(x, y, N):
    return 0 <= x < N and 0 <= y < N

# 반사 횟수를 셀 함수
cnt = 0

"""
    방향 전환 메모

    /
    - 오른쪽 -> 위쪽 0 3
    - 왼쪽 -> 아래쪽 2 1
    - 위쪽 -> 오른쪽 3 0 
    - 아래쪽 -> 왼쪽 1 2

    \\
    - 오른쪽 -> 아래쪽 0 1
    - 왼쪽 -> 위쪽 2 3
    - 위쪽 -> 왼쪽 3 2
    - 아래쪽 -> 오른쪽 1 0

"""

while True :
    # 범위 안에 없다면 반복문 종료
    if not (in_range(x, y, N)) :
        break

    if mat[x][y] == "/" :
        direc_num = 4 - (direc_num + 1)
    else : 
        if direc_num % 2 :
            direc_num += 1
        else :
            direc_num -= 1

    cnt += 1
    x += dx[direc_num]
    y += dy[direc_num]

print(cnt)




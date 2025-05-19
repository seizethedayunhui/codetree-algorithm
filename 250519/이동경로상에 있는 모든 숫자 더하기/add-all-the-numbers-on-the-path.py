N, T = map(int, input().split())

command = list(input())
cnt = 1

mat = list()
for _ in range(N) :
    row = list(map(int, input().split()))
    mat.append(row)

"""

    L : 왼쪽으로 90도 방향 전환
    R : 오른쪽으로 90도 방향 전환
    F : 바라보는 방향 한칸 이동

"""

dx = [ 0, 1, 0, -1 ]
dy = [ 1, 0, -1, 0 ]
direc_num = 3

# 범위 벗어나는지 확인하는 함수
def in_range(x, y, N):
    return ( 0 <= x < N ) and ( 0 <= y < N ) 

x, y = N // 2, N // 2
ans = mat[x][y]


for elem in command :
    if elem == "L":
        # 왼쪽으로 90도 방향 전환
        direc_num = ( direc_num + 3 ) % 4

    elif elem == "R" :
        # 오른쪽으로 90도 방향 전환
        direc_num = ( direc_num + 1 ) % 4

    else :

        nx = x + dx[direc_num]
        ny = y + dy[direc_num]

        # 이동 자체를 하면 안됨
        if in_range(nx, ny, N):
            
            x += dx[direc_num]
            y += dy[direc_num]
            ans += mat[x][y]
            


    

    



print(ans)


    


    

    


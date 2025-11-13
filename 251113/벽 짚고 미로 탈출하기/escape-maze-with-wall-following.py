N = int(input())

x, y = map(int, input().split())
x -= 1
y -= 1

mat = list()

for _ in range(N) :
    element = input()
    element_list = list()
    for e in element :
        element_list.append(e)
    mat.append(element_list)

# 범위 안에 있는지 확인하는 함수
def in_range(x, y) :
    return 0 <= x < N and 0 <= y < N

# 사방이 막혔는지 확인하는 함수 
def is_possible(x, y, direc) :

    right_direc = (direc + 1) % 4
    left_direc = (direc + 3) % 4

    nx = x + dx[direc]
    ny = y + dy[direc]

    right_nx = x + dx[right_direc]
    right_ny = y + dy[right_direc]

    left_nx = x + dx[left_direc]
    left_ny = y + dy[left_direc]

    if mat[left_nx][left_ny] == "#" and mat[right_nx][right_ny] == "#" and mat[nx][ny] == "#":
        return False
    
    return True


dx = [ 0, 1, 0, -1]
dy = [ 1, 0, -1, 0]

direc = 0

flag = True

time = 0

nx, ny = x, y


while in_range(nx, ny):

    nx += dx[direc]
    ny += dy[direc]
    
    # 한 번만 더 이대로 이동하면 탈출하는 경우
    if not in_range(nx, ny) :
        time += 1
        break

    if mat[nx][ny] == "." :

        next_drec = (direc + 1) % 4
        right_x = nx + dx[next_drec]
        right_y = ny + dy[next_drec]

        if mat[right_x][right_y] == "#" :
            # 이동
            time += 1
        else :
            # 일단 이동 -> nx, ny
            time += 1
            # 범위 벗어나면 탈출했다는 의미
            if not in_range(nx, ny) :
                break
                
            # 방향 전환
            direc = (direc + 1) % 4
            # 한번 더 이동
            time += 1
            nx += dx[direc]
            ny += dy[direc]

    else :

        if not is_possible(nx, ny, direc) :
            flag = False
            break  
        direc = (direc + 3) % 4

    # 처음의 위치로 돌아온 경우 탈출할 수 없다는 의미이므로 break
    if not direc and (nx == x and ny == y) :
        flag = False
        break
  



if flag :
    print(time)
else :
    print(-1)

    

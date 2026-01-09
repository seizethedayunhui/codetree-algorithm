from collections import deque

N, K = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]

start_x, start_y = map(int, input().split())
start_x -= 1
start_y -= 1

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

def can_go(x, y, target_val, visited_arr):
    # 범위 안이고, 방문한 적 없으며, 시작점의 숫자보다 작아야 함
    return in_range(x, y) and not visited_arr[x][y] and mat[x][y] < target_val

def bfs(x, y):
    curr_x, curr_y = x, y

    for _ in range(K):
        # 1. 매 이동(K)마다 BFS를 위한 초기화 필요
        visited = [[False for _ in range(N)] for _ in range(N)]
        points = deque([(curr_x, curr_y)])
        visited[curr_x][curr_y] = True
        
        target_val = mat[curr_x][curr_y] # 기준이 되는 시작점의 숫자
        
        max_value = -1
        next_x, next_y = -1, -1

        # 2. BFS 탐색을 통해 갈 수 있는 모든 지점 확인
        while points:
            cx, cy = points.popleft()
            
            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                
                if can_go(nx, ny, target_val, visited):
                    visited[nx][ny] = True
                    points.append((nx, ny))
                    
                    # 3. 문제의 우선순위 조건: 1.최댓값, 2.행 번호 작은 것, 3.열 번호 작은 것
                    # (next_x, next_y가 -1인 경우는 첫 후보 발견 시 무조건 업데이트)
                    if mat[nx][ny] > max_value:
                        max_value = mat[nx][ny]
                        next_x, next_y = nx, ny
                    elif mat[nx][ny] == max_value:
                        if nx < next_x:
                            next_x, next_y = nx, ny
                        elif nx == next_x:
                            if ny < next_y:
                                next_x, next_y = nx, ny

        # 4. 갈 수 있는 곳이 없으면(업데이트 안 됨) 바로 종료
        if next_x == -1:
            break
        
        # 다음 위치로 현재 위치 갱신
        curr_x, curr_y = next_x, next_y

    return curr_x, curr_y

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

final_x, final_y = bfs(start_x, start_y)
print(final_x + 1, final_y + 1) # 1을 다시 더해서 출력
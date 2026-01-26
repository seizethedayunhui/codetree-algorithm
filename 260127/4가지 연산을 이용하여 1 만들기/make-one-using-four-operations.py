from collections import deque

N = int(input())
q = deque()

def calc(idx, n):

    result = -1

    if idx == 0:
        result = n-1

    elif idx == 1:
        result = n+1
    
    elif idx == 2:
        if not n % 2:
           result = n // 2
    
    else :
        if not n % 3 :
            result = n // 3

    return result

def bfs(N):

    q = deque()
    cnt = 0

    visited = [False] * (N + 2)

    q.append((N, cnt))

    while q:
        n, current_cnt = q.popleft()

        if n == 1:
            return current_cnt

        for i in range(4):

            next_n = calc(i, n)

            if 1 <= next_n <= N + 1 and not visited[next_n]:
                q.append((next_n, current_cnt+1))
                visited[next_n] = True

ans = bfs(N)
print(ans)
            


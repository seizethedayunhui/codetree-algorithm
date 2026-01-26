from collections import deque

N = int(input())
q = deque()

def calc(idx, n):

    if idx == 0:
        return n-1

    elif idx == 1:
        return n+1
    
    elif idx == 2:
        if not n % 2:
            return n // 2
    
    else :
        if not n % 3 :
            return n // 3

    return n

def bfs(N):

    q = deque()
    cnt = 0

    q.append((N, cnt))

    while q:
        n, current_cnt = q.popleft()

        if n == 1:
            return current_cnt

        for i in range(4):

            next_n = calc(i, n)

            if next_n != n:
                q.append((next_n, current_cnt+1))

ans = bfs(N)
print(ans)
            

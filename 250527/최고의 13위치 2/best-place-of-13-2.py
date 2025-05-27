N = int(input())
mat = list()
for _ in range(N) :
    row = list(map(int, input().split()))
    mat.append(row)

dx = [ 0, 0, 0 ]
dy = [ 0, 1, 2 ]

def in_range(x, y, N) :
    return ( 0 <= x < N ) and ( 0 <= y < N )

max_cnt = float('-inf')
for x1 in range(N) :
    for y1 in range(N-2) :
        for x2 in range(x1+1, N) :


            for y2 in range(N-2) :

                # 여기서 0으로 초기화 해주어야함. 
                cnt1 = 0
                cnt2 = 0
                cnt = 0

                # 실질적으로 cnt하는 곳
                for i in range(3) :
                    cnt1 += mat[x1 + dx[i]][y1 + dy[i]]
                    cnt2 += mat[x2 + dx[i]][y2 + dy[i]]

                cnt = cnt1 + cnt2

                max_cnt = max(max_cnt, cnt)

print(max_cnt)

            
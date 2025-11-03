N, M = map(int, input().split())
mat = [ list(map(int, input().split())) for _ in range(N) ]

max_sum = float('-inf')

# x, y 시작좌표결정
for x in range(N) :
    for y in range(M) :
        # 가로 세로 길이 결정
        for w in range(N-x) :
            for h in range(M-y):
                current_sum1 = 0 
                # 넓이 결정 (가로 길이 / 세로 길이)
                for i in range(w+1) :
                    for j in range(h+1):
                        current_sum1 += mat[x+i][y+j]

                # 현재 사각형의 시작점과 끝점을 지정
                start_x, start_y = x, y 
                end_x, end_y = x + w, y + h

                # print(start_x, start_y, end_x, end_y, w, h, current_sum1)
            
                # 4방향 모두 탐색
                # x, y 좌표 결정
                max_sum2 = float('-inf')

                for x1 in range(start_x) :
                    for y1 in range(M) :
                        # 넓이 결정 후 탐색
                        for w1 in range(start_x-x1) :
                            for h1 in range(M-y1) :
                                current_sum2 = 0
                                for i in range(w1+1) :
                                    for j in range(h1+1) :
                                        current_sum2 += mat[x1+i][y1+j]
                                max_sum2 = max(max_sum2, current_sum2)

                for x2 in range(N) :
                    for y2 in range(start_y) :
                        # 넓이 결정 후 탐색
                        for w2 in range(N-x2) :
                            for h2 in range(start_y-y2) :
                                current_sum2 = 0
                                for i in range(w2+1) :
                                    for j in range(h2+1) :
                                        current_sum2 += mat[x2+i][y2+j]
                                max_sum2 = max(max_sum2, current_sum2)

                for x3 in range(end_x+1, N) :
                    for y3 in range(M) :
                        # 넓이 결정 후 탐색
                        for w3 in range(N-x3) :
                            for h3 in range(M-y3) :
                                current_sum2 = 0
                                for i in range(w3+1) :
                                    for j in range(h3+1) :
                                        current_sum2 += mat[x3+i][y3+j]
                                max_sum2 = max(max_sum2, current_sum2)

                for x4 in range(N) :
                    for y4 in range(end_y + 1, M) :
                        # 넓이 결정 후 탐색
                        for w4 in range(N-x4) :
                            for h4 in range(M-y4) :
                                current_sum2 = 0
                                for i in range(w4+1) :
                                    for j in range(h4+1) :
                                        current_sum2 += mat[x4+i][y4+j]
                                max_sum2 = max(max_sum2, current_sum2)

                current_max_sum = current_sum1 + max_sum2
                max_sum = max(max_sum, current_max_sum)

print(max_sum)

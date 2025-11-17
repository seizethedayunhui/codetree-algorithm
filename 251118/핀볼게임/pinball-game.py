N = int(input())

mat = [ list(map(int, input().split())) for _ in range(N) ]

x_axis = [ 0, N-1]
y_axis = [ 0, N-1]

max_time = float('-inf')
dx = [ 0, 1, 0, -1]
dy = [ 1, 0, -1, 0]

def in_range(x, y) :
    return 0<= x < N and 0 <= y < N

for x1 in x_axis :

    for y1 in range(N) :

        if x1 == 0 :
            direc_num = 1
        else :
            direc_num = 3

        current_time = 1
        nx, ny = x1, y1

        while(in_range(nx, ny)) :

            if mat[nx][ny] == 1 :
                if direc_num % 2 :
                    direc_num = (direc_num + 1) % 4
                else :
                    direc_num = (direc_num + 3) % 4
            elif mat[nx][ny] == 2 :
                if direc_num % 2 :
                    direc_num = (direc_num + 3) % 4
                else :
                    direc_num = (direc_num + 1) % 4

            nx += dx[direc_num]
            ny += dy[direc_num]
            current_time += 1
        #     print(nx, ny, direc_num)
        # print()
        
        max_time = max(current_time, max_time)


for y2 in y_axis :

    for x2 in range(N) :

        if y2 == 0 :
            direc_num = 0
        else :
            direc_num = 2

        current_time = 1
        nx, ny = x2, y2

        while(in_range(nx, ny)) :

            if mat[nx][ny] == 1 :
                if direc_num % 2 :
                    direc_num = (direc_num + 1) % 4
                else :
                    direc_num = (direc_num + 3) % 4
            elif mat[nx][ny] == 2 :
                if direc_num % 2 :
                    direc_num = (direc_num + 3) % 4
                else :
                    direc_num = (direc_num + 1) % 4

            nx += dx[direc_num]
            ny += dy[direc_num]
            current_time += 1
            # print(nx, ny)
        
        max_time = max(current_time, max_time)    

print(max_time)    
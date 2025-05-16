commands = list(input())

dx = [ 0, 1, 0, -1 ]
dy = [ 1, 0, -1, 0 ]

direc_idx = 3
time = 0
flag = False

x, y = 100000, 100000

for command in commands :
    if command == "L" :
        direc_idx = (direc_idx + 3) % 4
    elif command == "R" :
        direc_idx = (direc_idx + 1) % 4
    else :
        x += dx[direc_idx]
        y += dy[direc_idx]
    time += 1

    if time and (x == 100000 and y == 100000) :
        flag = True
        break

if flag :
    print(time)
else :
    print(-1)



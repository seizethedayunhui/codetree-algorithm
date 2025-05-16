# 총 움직이는 횟수 
N = int(input())

commands = list()

for _ in range(N) :

    d, s = input().split()
    s = int(s)

    command = (d, s)
    commands.append(command)

# 방향을 index로 변환
direc_to_id = {
    "E" : 0,
    "S" : 1,
    "W" : 2,
    "N" : 3
}

dx = [ 0, 1, 0, -1 ]
dy = [ 1, 0, -1, 0 ]

# 시작 위치 (100 * 10)
x, y = 1000, 1000

time = 0
flag = False

for command in commands :

    if (time > 0) and ( x == 1000 and y == 1000 ) :
        flag = True
        break

    idx = direc_to_id[command[0]]

    for _ in range(command[1]) :

        if time and ( x == 1000 and y == 1000 ) :
            flag = True
            break

        x += dx[idx]
        y += dy[idx]
        time += 1

if flag :
    print(time)
else :
    print(-1)

    

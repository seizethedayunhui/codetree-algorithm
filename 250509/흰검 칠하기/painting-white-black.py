N = int(input())

# 흰색 횟수, 검은색 횟수, 현재 색깔 -> W, B, G
vertical = [ [0, 0, ''] for _ in range(200000)]
current = 100000 # 시작위치

commands = list()

for _ in range(N) :

    size, di = input().split()
    size = int(size)

    commands.append((size, di))

for command in commands :

    # 일단 명령부터 체크
    # 명령이 right인 경우
    if command[1] == "R" :
        # 현재를 포함해서 크기만큼 검은색으로 색칠
        for i in range(command[0]) :

            # 이미 회색인 경우 아래 생략 :
            if vertical[current+i][2] == "G" :
                continue
            else :
                vertical[current + i][1] += 1
                vertical[current + i][2] = "B"

            if vertical[current + i][0] >=2 and vertical[current + i][1] >=2 :
                vertical[current + i][2] = "G"


        current += (command[0]-1)

    # 명령이 left인 경우
    else :
        for j in range(command[0]) :

            # 이미 회색인 경우 아래 생략 :
            if vertical[current-j][2] == "G" :
                continue
            else :
                vertical[current - j][0] += 1
                vertical[current - j][2] = "W"

            if vertical[current -  j][0] >=2 and vertical[current - j][1] >=2 :
                vertical[current - j][2] = "G"
        current -= (command[0]-1)


W_cnt = 0
B_cnt = 0
G_cnt = 0

for elem in vertical :

    if elem[2] == "W" :
        W_cnt += 1
    elif elem[2] == "B" :
        B_cnt += 1
    elif elem[2] == "G" :
        G_cnt += 1

print(f"{W_cnt} {B_cnt} {G_cnt}")










    
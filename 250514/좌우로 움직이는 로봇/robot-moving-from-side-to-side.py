# 각 로봇이 움직인 횟수
N, M = map(int, input().split())

A_commands = list()
B_commands = list()

for _ in range(N) :
    t, d = input().split()
    A_commands.append((int(t), d))

for _ in range(M) :
    t, d = input().split()
    B_commands.append((int(t), d))

A_current = 0
B_current = 0

A_move = [A_current]
B_move = [B_current]

for command in A_commands :
    if command[1] == "L" :
        for _ in range(command[0]) :
            A_current -= 1
            A_move.append(A_current)
    else :
        for _ in range(command[0]) :
            A_current += 1
            A_move.append(A_current)

for command in B_commands :
    if command[1] == "L" :
        for _ in range(command[0]) :
            B_current -= 1
            B_move.append(B_current)
    else :
        for _ in range(command[0]) :
            B_current += 1
            B_move.append(B_current)

cnt = 0

# 최대를 길이를 설정
move_len = max(len(A_move), len(B_move))

for i in range(move_len) :

    # 범위 조정 설정
    if len(A_move) <= i+1 :
        A_i = len(A_move) - 1
    else :
        A_i = i
    
    if len(B_move) <= i+1 :
        B_i = len(B_move) - 1
    else :
        B_i = i

    # 그냥 보통의 경우
    if (i != 0) and (A_move[A_i-1] != B_move[B_i-1]) :
        if A_move[A_i] == B_move[B_i] :
            cnt += 1  

print(cnt)

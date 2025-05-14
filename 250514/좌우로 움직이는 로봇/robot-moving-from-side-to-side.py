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


A_flag = False
B_flag = False
for i in range(move_len) :

    # 범위 조정 설정
    # 플래그로 구분

    # flag : 어느 배열에서 범위가 끝났는지 확인
    # #_idx : 이전의 위치를 알기 위한 idx
    # A_i : 현재의 로봇 위치
    
    if len(A_move) < i+1 :
        A_i = len(A_move) - 1
        A_flag = True
    else :
        A_i = i
    
    if len(B_move) < i+1 :
        B_i = len(B_move) - 1
        B_flag = True
    else :
        B_i = i

    # 그냥 보통의 경우
    if (i != 0) :

        A_idx = i-1
        B_idx = i-1

        # flag를 통해 어느 배열이 끝났는지 파악함
        if (A_flag == True) :
            # 끝난 위치로 인덱스 설정
            A_idx = A_i
        elif (B_flag == True) :
            # 끝난 위치로 인덱스 설정
            B_idx = B_i

        # 이전과 다른 위치라면 cnt += 1
        if (A_move[A_idx] != B_move[B_idx]) :
            if A_move[A_i] == B_move[B_i] :
                cnt += 1 

print(cnt)

N, M = map(int, input().split())

A_commands = list()
B_commands = list()

for _ in range(N) :
    v, t = map(int, input().split())
    A_commands.append((v, t))

for _ in range(M) :
    v, t = map(int, input().split())
    B_commands.append((v, t))

A_move = list()
B_move = list()

A_current = 0
B_current = 0

for command in A_commands :
    for _ in range(command[1]):
        A_current += command[0]
        A_move.append(A_current)

for command in B_commands :
    for _ in range(command[1]):
        B_current += command[0]
        B_move.append(B_current)

current_leader = list()
cnt = 0
for i in range(len(A_move)) :

    # 일단 선두가 없는 경우
    if not current_leader :
        if (A_move[i] > B_move[i]) :
            current_leader = ["A"]
            cnt += 1
        elif (B_move[i] > A_move[i]) :
            current_leader = ["B"]
            cnt += 1
        else :
            current_leader = ["A", "B"]
            cnt += 1

    # 선두가 있는데 달라지는 경우
    else :
        # 원래 선두 그룹이 2명이었던 경우
        if len(current_leader) == 2 :
            # 각각이 빨라지는 경우 계산
            if A_move[i] > B_move[i] :
                cnt += 1
                current_leader.remove("B")
            elif B_move[i] > A_move[i] :
                cnt += 1
                current_leader.remove("A")
        # 원래 선두그룹이 1명인 경우
        else :
            # 개수 안바뀌고 선수만 바뀌는 경우
            if (current_leader[0] != "A") and (A_move[i] > B_move[i]) :
                cnt += 1
                current_leader = ["A"]
            elif (current_leader[0] != "B") and (B_move[i] > A_move[i]) :
                cnt += 1
                current_leader = ["B"]
            # 개수도 바뀌고 선수도 바뀌는 경우
            elif A_move[i] == B_move[i] :
                cnt += 1
                current_leader = ["A", "B"]

print(cnt)





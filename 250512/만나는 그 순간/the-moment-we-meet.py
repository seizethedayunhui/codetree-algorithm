# 입력
N, M = map(int, input().split())

A_commands = list()
B_commands = list()

for _ in range(N) :

    d, t = input().split()
    t = int(t)
    A_commands.append((d, t))

for _ in range(M) :

    d, t = input().split()
    t = int(t)
    B_commands.append((d, t))

A_move = list()
B_move = list()

# 시작위치
A_current = 0
B_current = 0

for command in A_commands :

    if command[0] == 'L' :
        for i in range(command[1]) :
            A_current -= 1
            A_move.append(A_current)
    else :
        for i in range(command[1]) :
            A_current += 1
            A_move.append(A_current)

for command in B_commands :

    if command[0] == 'L' :
        for i in range(command[1]) :
            B_current -= 1
            B_move.append(A_current)
    else :
        for i in range(command[1]) :
            B_current += 1
            B_move.append(B_current)

meet_time = -1

for i in range(len(B_move)) :

    if A_move[i] == B_move[i] :
        meet_time = i + 1
        break

print(meet_time)





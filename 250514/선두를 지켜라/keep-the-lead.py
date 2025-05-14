N, M = map(int, input().split())

A_commands = []
B_commands = []

for _ in range(N) :
    command = tuple(map(int, input().split()))
    A_commands.append(command)

for _ in range(M) :
    command = tuple(map(int, input().split()))
    B_commands.append(command)

# 움직임 자체를 배열로 기록함
A_move = list()
B_move = list()

A_current = 0
B_current = 0
for command in A_commands :
    # 시간 별로 이동 위치 기록
    for i in range(command[1]):
        A_current += command[0]
        A_move.append(A_current)

for command in B_commands :
    # 시간 별로 이동 위치 기록
    for i in range(command[1]):
        B_current += command[0]
        B_move.append(B_current)

# 시작할 때는 동일 선상에서 출발함
# 현재 누가 앞서는지 기록함

# 처음에 leader 없음
leader = None
cnt = 0
for i in range(len(A_move)) :

    # 리더가 없는 경우 -> cnt 하지 않음
    if (leader is None) and (A_move[i] != B_move[i] ) :
        if A_move[i] > B_move[i] :
            leader = "A"
        else :
            leader = "B"


    # 리더가 있는 경우 -> 조건 체크 후 리더 변경
    if (leader == "A") and (B_move[i] > A_move[i]) :
        leader = "B"
        cnt += 1
    elif (leader == "B") and (A_move[i] > B_move[i]) :
        leader = "A"
        cnt += 1

print(cnt)


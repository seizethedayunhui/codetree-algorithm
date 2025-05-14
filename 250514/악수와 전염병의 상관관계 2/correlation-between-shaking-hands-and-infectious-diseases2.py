# N : 개발자 수
# T : 악수 횟수
# K : 전염 가능 max 수
# P : 처음 전염병에 걸린 개발자

N, K, P, T = map(int, input().split())

commands = list()

for _ in range(T) :
    t, x, y = map(int, input().split())
    cnt = 0

    command = [t, x, y, cnt]
    commands.append(command)

# 시간 순서대로 정렬
commands.sort(key = lambda x : x[0])

# memo -> [감염여부, 악수횟수]
memo = [ [0, 0] for _ in range(N) ]
memo[K-1][0] = 1

for command in commands :

    # 개발자 번호
    x = command[1] - 1
    y = command[2] - 1
    # 감염되었는지 확인 & 감염횟수 만족하는지 확인 -> 개발자 별로 각각 진행
    if memo[x][0] and memo[x][1] < K :

        # 감염된 사람끼리 만난 경우
        if memo[y][0] :
            memo[y][1] += 1
        else :
            memo[y][0] = 1
        memo[x][1] += 1

    elif memo[y][0] and memo[y][1] < K :
        # 감염된 사람끼리 만난 경우
        if memo[x][0] :
            memo[x][1] += 1
        else :
            memo[x][0] = 1
        memo[y][1] += 1     

for elem in memo :
    print(elem[0], end="")  
        


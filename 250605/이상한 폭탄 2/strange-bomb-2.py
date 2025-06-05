N, K = map(int, input().split())

bombs = list()

for _ in range(N) :

    bomb = int(input())

    bombs.append(bomb)

def front_check(location, K) :

    for i in range(K) :

        if location - (i+1) < 0 :
            return False

    return True

def back_check(location, K) :

    for i in range(K) :

        if location + (i+1) >= N :
            return False

    return True

max_num = -1

for i in range(N) :

    flag = False
    # 앞 부분 체크
    for j in range(K) :
        if (i - (j+1) >= 0) and bombs[i] == bombs[i - (j+1)] :
            flag = True
            current_num = bombs[i]
    # 뒷 부분 체크
    for k in range(K) :
        if (i + (k+1) < N) and bombs[i] == bombs[i + (k+1)] :
            flag = True
            current_num = bombs[i]

    if flag :
        max_num = max(max_num, current_num)

print(max_num)


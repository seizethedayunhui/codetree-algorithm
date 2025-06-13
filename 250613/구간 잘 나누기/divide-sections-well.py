N, M = map(int, input().split())

arr = list(map(int, input().split()))

def combinations(idx, pick, picks, M, N) :

    if len(pick) == M - 1 :
        # 값은 복사해서 넣어주어야 함.
        # 리스트는 이후에 계속 값이 바뀌기 때문에
        picks.append(pick[:])
        return

    if idx >= N - 1 :
        return
    

    # 재귀 탐색
    pick.append(idx)
    # 넣는 경우
    combinations(idx + 1, pick, picks, M, N)

    # 넣지 않는 경우
    pick.pop()
    combinations(idx + 1, pick, picks, M, N)

pick = []
picks = []

# 재귀 탐색으로 가능한 조합수를 모두 구함
combinations(0, pick, picks, M, N)

min_max_sum = float('inf')
for pick in picks :

    current_max_sum = float('-inf')
    start = 0

    for elem in pick :
        current_sum = 0
        for i in range(start, elem+1):
            current_sum += arr[i]
        start = elem + 1
        current_max_sum = max(current_max_sum, current_sum)

    current_sum = 0
    for i in range(start, N):
        current_sum += arr[i]
    current_max_sum = max(current_max_sum, current_sum)
    
    min_max_sum = min(min_max_sum, current_max_sum)

print(min_max_sum)
        


        




    
    
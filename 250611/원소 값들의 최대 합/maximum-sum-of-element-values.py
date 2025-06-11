N, M = map(int, input().split())

num_list = list(map(int, input().split()))

max_sum = float('-inf')

# 시작 위치 결정
for i in range(N) :

    current_sum = 0
    location = i

    for j in range(M) :
        current_sum += num_list[location]
        location = (num_list[location] - 1 )

    max_sum = max(max_sum, current_sum)

print(max_sum)

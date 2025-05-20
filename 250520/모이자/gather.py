N = int(input())
A_list = list(map(int, input().split()))

min_distance = float('inf')

for i in range(N):

    current_distance = 0
    for j in range(N):
        current_distance += abs(j-i) * A_list[j]

    if current_distance < min_distance :
        min_distance = current_distance

print(min_distance)

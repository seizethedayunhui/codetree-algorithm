N = int(input())
num_list = list(map(int, input().split()))

min_gap = float('inf')

for i in range(N) :
    for j in range(i+1, N) :
        current_gap = abs(num_list[i] - num_list[j])
        if current_gap < min_gap :
            min_gap = current_gap

print(min_gap)
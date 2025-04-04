N = int(input())
num_list = list(map(int, input().split()))

min_cnt = 0
min_val = float('inf')

for num in num_list :
    if num < min_val :
        min_val = num
        min_cnt = 1
    elif num == min_val :
        min_cnt += 1
print(f"{min_val} {min_cnt}")



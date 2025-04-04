num_list = list(map(int, input().split()))

max_val = float('-inf')

for num in num_list :
    if num > max_val :
        max_val = num

print(max_val)
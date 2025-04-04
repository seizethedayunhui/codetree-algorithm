num_list = list(map(int, input().split()))

max_val = float('-inf')
min_val = float('inf')

for num in num_list :

    if num == 999 or num == -999 :
        print(f"{max_val} {min_val}")
        break
    
    if num > max_val :
        max_val = num
    if num < min_val :
        min_val = num
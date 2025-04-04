N = int(input())
num_list = list(map(int, input().split()))

dup_list = list()

max_val = -1
prev_max_val = -1

for num in num_list :
    
    if num == max_val :
        # 두번째로 큰 값
        max_val = prev_max_val
        if max_val in dup_list :
            max_val = -1
        continue

    if num > max_val :
        prev_max_val = max_val
        max_val = num 
    elif num > prev_max_val :
        prev_max_val = num
    dup_list.append(num)
    

    
print(max_val)
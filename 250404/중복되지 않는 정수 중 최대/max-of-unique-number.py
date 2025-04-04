N = int(input())
num_list = list(map(int, input().split()))

dup_list = list()
prev_list = list()

max_val = -1
prev_max_val = -1

for num in num_list :
    
    if num == max_val :
        # 중복되는 값이 나온 경우 / 중복 배열에 넣음. 
        dup_list.append(num)
        max_val = prev_max_val
        if max_val in dup_list  :
            max_val = -1
        continue
    elif num in prev_list :
        dup_list.append(num)
        continue

    # 값이 max인 경우
    # max로 설정 후 prev_max도 설정
    if num > max_val :
        prev_max_val = max_val
        max_val = num 
    # 아닌데 prev_max 보다는 큰 경우 prev_max로 설정
    elif num > prev_max_val :
        prev_max_val = num
    # 이전에 지나간 값을 넣음. 
    prev_list.append(num)

    
print(max_val)
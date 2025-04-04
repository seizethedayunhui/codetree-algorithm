N = int(input())
num_list = list(map(int, input().split()))

dup_list = list()

max_val = -1
prev_max_val = -1

for num in num_list :
    
    # 일단 최댓값
    if num > max_val :
        max_val = num

    elif num == max_val :
        max_val = -1
    
       


if max_val == float('-inf') :
    print(-1)
else :
    print(max_val)
    


    
    
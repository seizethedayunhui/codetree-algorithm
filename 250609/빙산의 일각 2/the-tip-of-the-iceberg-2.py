N = int(input())

height_list = list()

for _ in range(N) :
    height = int(input())
    height_list.append(height)


max_cnt = float('-inf')
for H in range(1, 10001) :

    current_cnt = 0
    continue_flag = False

    for i in range(N) :

        if not continue_flag :
            if height_list[i] > H :
                continue_flag = True
        else :
            if height_list[i] <= H :
                current_cnt += 1
                continue_flag = False
    
    if continue_flag :
        current_cnt += 1

    max_cnt = max(max_cnt, current_cnt)

print(max_cnt)

 


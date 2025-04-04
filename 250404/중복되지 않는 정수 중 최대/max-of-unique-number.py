N = int(input())
num_list = list(map(int, input().split()))


max_val = -1
prev_max_val = -1

# 카운팅 하는 방식으로 구현함
for num in num_list :
    if num > max_val :
        cnt = 0
        for elem in num_list:
            if elem == num :
                cnt += 1
        if cnt == 1 :
            max_val = num
            
    
    
print(max_val)
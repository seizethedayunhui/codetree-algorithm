num_list = list(map(int, input().split()))

standard_num = 500

# 500보다 작은 수 중에 가장 큰 수 - 500과의 차가 가장 작은 수 
max_num = 0
gap1 = float('inf')

# 500 보다 큰 수 중에 가장 작은 수 - 500과의 차가 가장 작은 수
min_num = 0
gap2 = float('inf')

for num in num_list :

    # 중복되는 코드이므로 abs 사용하여 절댓값 처리
    current_gap = abs(num -  500)
    if num > 500 :
        if current_gap < gap2 :
            gap2 = current_gap
            min_num = num

    else :
        if current_gap < gap1 :
            gap1 = current_gap
            max_num = num

print(max_num, min_num)
X, Y = map(int, input().split())

cnt = 0
for num in range(X, Y+1) :

    num_list = list()
    while (num != 0) :
        num_list.append(num % 10)
        num //= 10
    
    num_list.sort()
    standard = num_list[0]
    diff_cnt = 0
    same_cnt = 0

    for i in range(1, len(num_list)) :

        if standard != num_list[i] :
            standard = num_list[i]
            diff_cnt +=1
        else :
            same_cnt += 1
    
    # 주류인경우
    if same_cnt == len(num_list) - 2 and diff_cnt == 1 :
        cnt += 1



print(cnt)


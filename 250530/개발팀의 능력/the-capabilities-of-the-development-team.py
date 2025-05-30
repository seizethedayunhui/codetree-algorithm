exp_list = list(map(int, input().split()))

def min_max_exp(sum1, sum2, sum3) :

    if sum1 > sum2 and sum1 > sum3 :
        max_sum = sum1
    elif sum2 > sum1 and sum2 >sum3 :
        max_sum = sum2
    else :
        max_sum = sum3

    if sum1 < sum2 and sum1 < sum3 :
        min_sum = sum1
    elif sum2 < sum1 and sum2 < sum3 :
        min_sum = sum2
    else :
        min_sum = sum3

    return min_sum, max_sum

def calc_exp(i, j, k, l, exp_list) :

    # 나머지 하나 구하기
    for exp in range(5):

        if exp not in [i, j, k, l] :
            m = exp
            break

    exp1_sum = exp_list[i] + exp_list[j]
    exp2_sum = exp_list[k] + exp_list[l]
    exp3_sum = exp_list[m]

    # 능력치 합이 같은 경우
    if exp1_sum == exp2_sum or exp2_sum == exp3_sum or exp3_sum == exp1_sum :
        return 0

    min_sum, max_sum = min_max_exp(exp1_sum, exp2_sum, exp3_sum)

    return max_sum - min_sum

    
min_diff = float('inf')
flag = False

for i in range(5) :
    for j in range(5) :
        for k in range(5) :
            for l in range(5) :

                if i == j or i == k or i == l or j == k or j == l or k == l :
                    continue

                current_diff = calc_exp(i, j, k, l, exp_list)

                if current_diff :
                    min_diff = min(min_diff, current_diff)
                    flag = True

if flag :
    print(min_diff)
else :
    print(-1)

                
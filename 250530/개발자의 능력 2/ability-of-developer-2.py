exp_list = list(map(int, input().split()))

def min_max_exp(sum1, sum2, sum3) :

    if sum1 >= sum2 and sum1 >= sum3 :
            max_sum = sum1
    elif sum2 >= sum1 and sum2 >= sum3 :
            max_sum = sum2
    else :
        max_sum = sum3

    if sum1 <= sum2 and sum1 <= sum3 :
            min_sum = sum1
    elif sum2 <=  sum1 and sum2 <= sum3 :
            min_sum = sum2
    else :
        min_sum = sum3

    return min_sum, max_sum


def calc_exp(i, j, k, l, exp_list) :

    exp3_idx = list()

    for idx in range(6) :
        if not(idx in [i, j, k, l]) :
            exp3_idx.append(idx)
    
    exp1_sum = exp_list[i] + exp_list[j]
    exp2_sum = exp_list[k] + exp_list[l]
    exp3_sum = exp_list[exp3_idx[0]] + exp_list[exp3_idx[1]]
    # print(i,j, k, l, exp3_idx)
    min_sum, max_sum = min_max_exp(exp1_sum, exp2_sum, exp3_sum)

    return abs(max_sum - min_sum)



min_diff = float('inf')

for i in range(6) :
    for j in range(6) :
        for k in range(6) :
            for l in range(6) :

                if ( i == j ) or ( i == k ) or ( i == l ) or ( j == k ) or ( j == l ) or ( k == l )  :
                    continue

                exp_diff = calc_exp(i, j, k, l, exp_list)
                min_diff = min(min_diff, exp_diff)

print(min_diff)

                

                

            
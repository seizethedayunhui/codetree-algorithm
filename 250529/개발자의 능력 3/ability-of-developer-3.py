ability = list(map(int, input().split()))

def calc_exp_diff(i, j, k, ability) :

    exp_sum1 = ability[i] + ability[j] + ability[k]
    exp_sum2 = 0
    for exp in range(6) :
        if (i != exp ) and (j != exp ) and ( k != exp ) :
            exp_sum2 += ability[exp]

    return abs(exp_sum1-exp_sum2)

min_diff_exp = float('inf')

for i in range(6):
    for j in range(i+1, 6):
        for k in range(j+1, 6):
            current_diff_exp = calc_exp_diff(i, j, k, ability)

            min_diff_exp = min(min_diff_exp, current_diff_exp)

print(min_diff_exp)
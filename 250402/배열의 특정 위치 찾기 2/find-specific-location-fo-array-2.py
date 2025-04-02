num_list = list(map(int, input().split()))

odd_sum = 0
even_sum = 0
for i in range(10) :
    if i % 2 :
        even_sum += num_list[i]
    else :
        odd_sum += num_list[i]

sum_max = max(odd_sum, even_sum)
sum_min = min(odd_sum, even_sum)

print(sum_max - sum_min)
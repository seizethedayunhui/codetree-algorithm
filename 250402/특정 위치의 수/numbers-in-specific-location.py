num_list = list(map(int, input().split()))

ans_sum = 0
for i in range(10) :
    if i+1 == 3 or i+1 == 5 or i+1 == 10 :
        ans_sum +=num_list[i]

print(ans_sum)
num_list = list(map(int, input().split()))

for i in range(len(num_list)) :
    if not num_list[i] :
        num_list = num_list[:i]
        break

num_sum = 0
num_len = len(num_list)

for num in num_list :
    num_sum += num

num_avg = num_sum / num_len

print(f"{num_sum} {num_avg:.1f}")
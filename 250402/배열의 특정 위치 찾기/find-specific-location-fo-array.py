num_list = list(map(int, input().split()))

mul3_sum = 0

for i in range(2, 10, 3) :
    mul3_sum += num_list[i]

mul3_avg = mul3_sum / 3

even_sum = 0
for j in range(10) :
    if j % 2 :
        even_sum += num_list[j]

print(f"{even_sum} {mul3_avg:.1f}")
        
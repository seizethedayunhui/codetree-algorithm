num_list = list(map(int, input().split()))

even_sum = 0
even_cnt = 0

for num in num_list :
    if not num :
        break
    
    if num % 2 == 0 :
        even_sum += num
        even_cnt += 1

print(f"{even_cnt} {even_sum}")
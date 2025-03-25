N_list = [ int(input()) for _ in range(10) ]

mul3_cnt = 0
mul5_cnt = 0

for number in N_list :

    if number % 3 == 0:
        mul3_cnt += 1
    
    if number % 5 == 0 :
        mul5_cnt += 1

print(mul3_cnt, mul5_cnt)
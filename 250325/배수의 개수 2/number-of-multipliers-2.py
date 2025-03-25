N_list = [ int(input()) for _ in range(10) ]
cnt = 0

for number in N_list :
    if number % 2 :
        cnt += 1

print(cnt)
temp_list = [ list(map(str, input().split())) for _ in range(3) ]

check_a = 0

for temp in temp_list :
    if int(temp[1]) >= 37 :
        if temp[0] == 'Y' :
            check_a += 1

if check_a >= 2 :
    print('E')
else :
    print('N')

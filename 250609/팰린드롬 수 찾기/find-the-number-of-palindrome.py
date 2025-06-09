X, Y = map(int, input().split())

def num_to_list(n) :

    num_list = list()
    while ( n != 0 ) :
        num_list.append(n % 10)
        n //= 10
    
    return num_list

cnt = 0
for n in range(X, Y+1) :

    num_list = num_to_list(n)
    flag = True

    for i in range( len(num_list)//2 ) :

        if num_list[i] != num_list[len(num_list)-1-i] :
            flag = False
            break
    if flag :
        cnt += 1

print(cnt)


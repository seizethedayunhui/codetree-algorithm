num_list = list(map(int, input().split()))

for num in num_list :
    if not num :
        break
    
    if num % 2 :
        print( num + 3 , end=" ")
    else :
        print ( int(num//2), end=" ")
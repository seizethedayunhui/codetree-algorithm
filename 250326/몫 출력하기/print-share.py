cnt = 3

while True :

    if cnt == 0 :
            break
            
    num = int(input())

    if ( num % 2 ) :
        continue
    else :
        cnt -= 1
        print(int(num // 2))
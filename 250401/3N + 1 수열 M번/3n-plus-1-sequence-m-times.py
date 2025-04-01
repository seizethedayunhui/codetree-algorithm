M = int(input())
N = [ int(input()) for _ in range(M) ]

for num in N :
    cnt = 0
    while True :
        if num == 1 :
             print(cnt)
             break

        if num % 2 :
            num = 3*num + 1
        else :
            num //= 2
        cnt += 1
            
   
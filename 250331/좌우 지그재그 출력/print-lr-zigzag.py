N = int(input())

cnt = 1
for i in range(N) :
    
    if i % 2 :
        cnt += (N-1)
        for _ in range(N):
            print(cnt, end=" ")
            cnt -= 1
    else : 
        cnt += (N+1)
        if i == 0 :
            cnt = 1
        for _ in range(N):
            print(cnt, end=" ")
            cnt += 1
    print()

    
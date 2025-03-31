N = int(input())

cnt = 1
for i in range(N) :
    for _ in range(i) :
        print(" ", end=" ")
    for _ in range(N-i) :
        if cnt == 10 :
            cnt = 1
        print(cnt, end=" ")
        cnt += 1
    print()
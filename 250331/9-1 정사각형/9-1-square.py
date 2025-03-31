N = int(input())

cnt = 9
for _ in range(N) :
    for _ in range(N) : 
        if not cnt :
            cnt = 9
        print(cnt, end="")
        cnt -= 1
    print()
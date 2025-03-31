n = int(input())

cnt = 1
for i in range(n) :

    # 홀수 행일 때
    if i % 2 :
        for j in range(n) :
            print(cnt, end = " ")
            cnt += 2
        cnt -= 1
    else :
        for k in range(n) :
            print(cnt, end=" ")
            cnt += 1
        cnt += 1
    print()
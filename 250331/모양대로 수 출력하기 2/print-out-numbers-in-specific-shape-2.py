N = int(input())

cnt = 1
for i in range(N) :
    for _ in range(N) :

        # 항상 8이하의 짝수만 등장해야하기 때문제 조건 설정
        if cnt >=5 :
            cnt = 1

        print ( 2 * cnt, end=" ")
        cnt += 1
    print() 
N = int(input())

ab_list = [ list(map(int, input().split())) for _ in range(N) ]

for a, b in ab_list :
    even_cnt = 0
    for i in range(a, b+1) :
        # 짝수인 경우 cnt 증가
        if i % 2 == 0 :
            even_cnt += i
    print(even_cnt)



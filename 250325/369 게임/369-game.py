N = int(input())

for i in range(1, N+1) :

    # 3의 배수인 경우 
    if i % 3 == 0 :
        print(0, end=" ")
        continue
        
    # i 가 두자리 수인 경우
    if i % 100 :
        # 십의 자리 수
        tens = i // 10
        # 일의 자리 수
        ones = i % 10

        if tens in [3, 6, 9] or ones in [3, 6, 9] :
            print(0, end=" ")
        else :
            print(i, end=" ")

    # i가 한자리 수인 경우
    else :
        ones = i % 10
        if  ones in [3, 6, 9] :
            print(0, end=" ")
        else :
            print(i, end=" ")

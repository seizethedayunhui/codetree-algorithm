N = int(input())

guess_list = list()

for _ in range(N) :
    guess = list(map(int, input().split()))
    guess_list.append(guess)

# 1번 카운트는 동일한 자리에 있는 경우
# 2번 카운트는 수는 같은데 다른 자리에 있는 경우


def hunds_tens_ones(num) :

    hunds = num // 100
    tens = ( num % 100) // 10
    ones = num % 10

    return hunds, tens, ones


# num1 내가 예측한 수, num2 입력으로 주어진 예측한 수
def comp_num(num1, num2) :

    cnt1 = 0
    cnt2 = 0

    for i in range(3) :

        # 값도 같고 자리도 같은 경우
        if num1[i] == num2[i] :
            cnt1 += 1
        # 값은 같지만 자리는 다른 경우
        elif (num1[i] != num2[i] ) and (num2[i] in num1) :
            cnt2 += 1
    
    return cnt1, cnt2

cnt = 0

for i in range(1,10) :
    for j in range(1, 10) :
        for k in range(1, 10) :

            # 하나라도 같은 값이 있는 경우 밑에 조건 탐색 X
            if ( i == j ) or ( j == k ) or ( k == i ) :
                continue

            num1 = [i, j, k]

            # 추측 리스트 
            for guess in guess_list :

                cnt_flag = True

                hunds, tens, ones = hunds_tens_ones(guess[0])
                num2 = [hunds, tens, ones]
                cnt1, cnt2 = comp_num(num1, num2)


                if guess[1] != cnt1 or guess[2] != cnt2 :
                    cnt_flag = False
                    break

            if cnt_flag :
                cnt += 1

                    

print(cnt)





            


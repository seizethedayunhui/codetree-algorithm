N = int(input())

arr = list(map(int, input().split()))

# 짝수에서 시작해서 짝, 홀 반복
# but, 주어진 순서에 상관없이도 가능

even_list = list()
odd_list = list()

# 짝수 홀수 분류
for num in arr :
    if num % 2 :
        odd_list.append(num)
    else :
        even_list.append(num)

odd_list.sort()
even_list.sort()

cnt = 0
odd_cnt = 0
even_cnt = 0

ans_list = list()

# print(odd_list, even_list)

for i in range(N) :
    current_list = list()
    # print(i)
    # 홀수가 와야하는 경우
    if i % 2 :
        # 짝수를 다 사용한경ㅇ + 원래 홀수의 개수가 홀수인 경우 + 남은 홀수의 개수가 홀수인 경우
        if even_cnt >= len(even_list) and (len(odd_list) - odd_cnt) % 2 and len(odd_list) % 2 :
                for _ in range(3) :
                    current_list.append(odd_list[odd_cnt])
                    odd_cnt += 1
                cnt += 1
        # 보통의 경우
        else :
            cnt += 1
            current_list.append(odd_list[odd_cnt])
            odd_cnt += 1
    # 짝수가 와야하는 경우
    else :
        # 짝수가 없는 경우 ->홀수 두개로 대체
        if even_cnt >= len(even_list) :
            for i in range(2) :
                current_list.append(odd_list[odd_cnt])
                odd_cnt += 1
            cnt += 1
        # 홀수를 다 사용하고 짝수만 남은 경우
        elif odd_cnt >= len(odd_list) :
            for j in range(even_cnt, len(even_list)) :
                current_list.append(even_list[j])
                even_cnt += 1
            cnt += 1
        # 보통의 경우 - 짝수 위치에는 짝수 하나만 있도록 함. 
        else :
            cnt += 1
            current_list.append(even_list[even_cnt])
            even_cnt += 1

    # print(current_list)
    ans_list.append(current_list)

    if odd_cnt + even_cnt >= N :
        break

# print(ans_list)
print(cnt)

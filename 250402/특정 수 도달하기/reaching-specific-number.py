num_list = list(map(int, input().split()))

# 250 이하의 수만 append 하는 리스트
ans_list = []
for i in range(len(num_list)) :

    # 만약 인덱스가 -1 이거나, 250 이상인 수가 나오면 즉시 break
    if i == len(num_list) -1 or num_list[i] >= 250 :
        break
    # 앞의 조건을 만족하지 않는 경우 list에 append
    else:
        ans_list.append(num_list[i])

# 평균을 구하기 위한 ans_list 원소의 합
num_sum = 0
for number in ans_list :
    num_sum += number

# 평균 구하기
avg = num_sum / len(ans_list)

print(f"{num_sum} {avg:.1f}")
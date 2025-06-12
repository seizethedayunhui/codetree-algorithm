N = int(input())
partial = list(map(int, input().split()))
digits = [ 0 for _ in range( N+1 ) ]

answers = list()

# 수열의 첫번째 원소를 결정함. 
for i in range(1, N + 1) :

    # 첫번째 조건을 만족시키지 않은 경우 continue
    if (i) >= partial[0] :
        continue

    picks = list()
    picks.append(i)
    digits[i] = 1

    prev_elem = i

    flag = True
    for elem in partial :

        # 현재 갑이 한 번도 등장하지 않은 경우
        if elem - prev_elem >= 1 and (digits[elem - prev_elem] != 1):
            prev_elem = (elem - prev_elem)
            digits[prev_elem] = 1          
            picks.append(prev_elem)
        # 앞의 조건을 만족시키지 않으면 break
        else :
            flag = False
            break

    if flag :
        answers.append(picks)

    # 모든 원소 값을 원래대로 돌려줌.
    for elem in picks :
        digits[elem] = 0

# 여러 개의 답이 있는 경우 사전식으로 가장 앞에오는 값을 선택
answers.sort()

for answer in answers[0] :
    print(answer, end=" ")


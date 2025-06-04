N, B = map(int, input().split())

price_list = list()

for _ in range(N) :

    price = int(input())
    price_list.append(price)

# 가장 많은 학생들에게 선물을 사주어야 하기 때문에, 원하는 선물의 가격이 작은 값부터 넣어주어야 최대한 많은 학생들에게 선물을 사줄 수 있음. 
price_list.sort(lambda x : x)

# 출력값
max_students = float('-inf')


for i in range(N) :

    # 현재 선물 산 선물 가격의 총합, 선택되는 학생이 바뀔 때마다 초기화 해주어야 함. 
    price_sum = 0

    # 현재 선물을 받는 학생 수
    cnt = 0

    for j in range(N) :

        if ( i == j ) :
            # i -> 50퍼 할인 받는 학생
            price_sum += (price_list[j] // 2) 
        else :
            price_sum += price_list[j]

        # 범위 벗어나는 경우 break, 아닌 경우 학생 수 증가
        if price_sum > B :
            break
        else :
            cnt += 1
            if price_sum == B :
                break

    max_students = max(max_students, cnt)

print(max_students)

        


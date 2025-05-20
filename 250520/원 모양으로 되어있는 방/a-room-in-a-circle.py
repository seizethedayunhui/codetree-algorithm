# N개의 방이 있다는 의미
N = int(input())

people = list()

for _ in range(N):
    num = int(input())
    people.append(num)


min_distance = float('inf')

# 가장 바깥쪽의 반복문은 방의 번호의 수를 나타냄
for i in range(N) :
    current_distance = 0
    start = i
    # 방을 돈다 -> N번의 이동
    for _ in range(N) :

        if start >= N :
            start = 0
        
        # i보다 현재가 작은 경우
        if start < i :
            current_distance += (people[start] * abs(N - (i-start)))

        # 같은 경우
        else :
            current_distance += (people[start] * abs(i - start))

        start += 1

    min_distance = min(min_distance, current_distance)

print(min_distance)


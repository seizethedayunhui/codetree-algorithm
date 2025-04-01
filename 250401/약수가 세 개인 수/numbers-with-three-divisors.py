start, end = map(int, input().split())

# 정답을 세는 cnt 변수
cnt = 0
for i in range(start, end+1) :
    # 약수의 개수를 세는 함수
    measure_cnt = 0
    for j in range(1, i+1) :
        # 약수 구해서, cnt 증가
        if i % j == 0 :
            measure_cnt += 1
    # 약수가 3개인 경우 cnt 증가
    if measure_cnt == 3:
        cnt += 1
print(cnt)
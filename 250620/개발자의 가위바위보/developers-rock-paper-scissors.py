N = int(input())

records = list()

for _ in range(N) :

    record = tuple(map(int, input().split()))
    records.append(record)

conditions = [["가위", "바위", "보"], ["가위", "보", "바위"], ["바위", "가위", "보"], ["바위", "보", "가위"],["보", "가위", "바위"], ["보", "바위", "가위"]]


max_cnt = float('-inf')
for condition in conditions :

    cnt = 0
    # 각 인덱스와 일치시키기....???
    for record in records :

        if condition[record[0]-1] == "가위" and condition[record[1]-1] == "보" :
            cnt += 1
        elif condition[record[0]-1] == "바위" and condition[record[1]-1] == "가위":
            cnt += 1
        elif condition[record[0]-1] == "보" and condition[record[1]-1] == "바위" :
            cnt += 1

    max_cnt = max(max_cnt, cnt)
    # print(condition, max_cnt)

print(max_cnt)
start, end = map(int, input().split())

cnt = 0

for i in range(start, end+1) :
    measure_list = []
    for j in range(1, i) :
        if i % j == 0 :
            measure_list.append(j)
    measure_sum = 0
    for measure in measure_list :
        measure_sum += measure
    if measure_sum == i :
        cnt += 1
print(cnt)
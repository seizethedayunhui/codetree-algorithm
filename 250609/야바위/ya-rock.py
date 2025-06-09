N = int(input())

records = list()

for _ in range(N) :

    record = list(map(int, input().split()))

    records.append(record)

max_cnt = float('-inf')

for i in range(3) :

    cups = [ 0 for _ in range(3) ]
    cups[i] = 1
    cnt = 0

    for record in records :

        a, b, c = record
        temp = cups[a-1]
        cups[a-1] = cups[b-1]
        cups[b-1] = temp

        if cups[c-1] :
            cnt += 1

    if cnt > max_cnt :
        max_cnt = cnt
        idx = i+1

print(idx)    

N = int(input())

lines = list()

for _ in range(N) :

    line = tuple(map(int, input().split()))
    lines.append(line)

cnt = 0
for i in range(N-2) :
    for j in range(i+1, N) :
        for k in range(j+1, N) :

            records = [ 0 for _ in range(101) ]

            for l in range(N) :

                if l != i and l != j and l != k :
                    for m in range(lines[l][0], lines[l][1]+1) :
                        records[m] += 1

            flag = True
            # print(records)
            for record in records :
                if record >= 2 :
                    flag = False
                    break
            if flag :
                cnt += 1

print(cnt)



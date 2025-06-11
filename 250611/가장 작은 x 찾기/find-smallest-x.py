N = int(input())

ranges = list()

for _ in range(N) :

    a, b = map(int, input().split())

    ranges.append((a,b))


for i in range(1, 10000) :

    flag = True

    for j in range(N) :
        if i * ( 2 ** (j+1) ) < ranges[j][0] or i * ( 2 ** (j+1) ) > ranges[j][1] :
            flag = False
            break

    if flag :
        print(i)
        break
N = int(input())

lines = list()
for _ in range(N) :
    line = tuple(map(int, input().split()))
    lines.append(line)

records = [ 0 for _ in range(101) ]

for line in lines :

    for i in range(line[0], line[1] + 1) :
        records[i] += 1

flag = False
for record in records :
    if record >= 2 :
        flag = True
        break

if flag :
    print("Yes")
else :
    print("No")
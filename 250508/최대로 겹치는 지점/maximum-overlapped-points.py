N = int(input())
lines = list()

for _ in range(N):

    line = tuple(map(int, input().split()))
    lines.append(line)

vertical = [0] * 100

for elem in lines :

    for i in range(elem[0]-1, elem[1]) :
        vertical[i] += 1


ans = float('-inf')
for elem in vertical :

    if elem > ans :
        ans = elem

print(ans)
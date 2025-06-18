location = list(map(int, input().split()))
location.sort() # 최소 위치..

gap = 0
cnt = 0

while (gap != 2) :

    if (location[1] - location[0] > location[2] - location[1]) :

        temp = location[1]
        location[1] = (temp + location[0]) // 2 
        location[2] = temp

    else :

        temp = location[1]
        location[1] = (temp + location[2]) // 2 
        location[0] = temp

    gap = abs(location[1]-location[0]) + abs(location[2]-location[1])
    cnt += 1

print(cnt)





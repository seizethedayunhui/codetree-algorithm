location = list(map(int, input().split()))
location.sort() 

cnt = 0
gap = abs(location[1]-location[0]) + abs(location[2]-location[1])

while (gap != 2) :

    gap1 = location[1] - location[0]
    gap2 = location[2] - location[1]

    if (gap1 == 1) :

        temp = location[1]

        if (((location[2] - location[1]) % 2)) :
            location[1] = (temp + location[2]) // 2 + 1
        else :
            location[1] = (temp + location[2]) // 2
        
        location[0] = temp

    elif (gap1 < gap2) :

        temp = location[1]

        if (((location[1] - location[0]) % 2)) :
            location[1] = (temp + location[0]) // 2 + 1
        else :
            location[1] = (temp + location[0]) // 2
            
        location[2] = temp

    elif (gap2 == 1) :

        temp = location[1]

        if (((location[1] - location[0]) % 2)) :
            location[1] = (temp + location[0]) // 2 + 1
        else :
            location[1] = (temp + location[0]) // 2
            
        location[2] = temp

    else :
        temp = location[1]

        if (((location[2] - location[1]) % 2)) :
            location[1] = (temp + location[2]) // 2 + 1
        else :
            location[1] = (temp + location[2]) // 2
        
        location[0] = temp

    gap = abs(location[1]-location[0]) + abs(location[2]-location[1])
    cnt += 1
    # print(location)

print(cnt)





location = list(map(int, input().split()))
location.sort() 

cnt = 0
flag = (location[1] - location[0] == 1) and (location[2] - location[1] == 1)

while not flag :

    # 각 숫자들의 gap
    gap1 = location[1] - location[0]
    gap2 = location[2] - location[1]

    # gap이 2인 경우 -> 범위조절
    if gap1 == 2 :

        temp = location[1]

        location[1] = location[1] - 1
        location[2] = temp
    
    elif gap2 == 2 :
        
        temp = location[1]

        location[1] = location[1] + 1
        location[0] = temp

    # 일단 gap이 작은 것을 pick, 하지만 gap이 큰데 상대방 gap이 1인 경우엔 조정
    elif gap1 < gap2  or (gap1 > gap2 and gap2 == 1):
        temp = location[1]

        location[1] = location[1] - 2
        location[2] = temp

    elif gap2 < gap1 or (gap2 > gap1 and gap1 == 1):

        temp = location[1]

        location[1] = location[1] + 2
        location[0] = temp


    cnt += 1
    flag = (location[1] - location[0] == 1) and (location[2] - location[1] == 1)

    # print(location)
print(cnt)





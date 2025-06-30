s1, s2, s3 = map(int, input().split())

gap1 = abs(s2 - s1)
gap2 = abs(s3 - s2)

cnt = 0

while not (gap1 == 1 and gap2 == 1) :

    if gap1 >= gap2 :

        temp = s2

        s2 = s1 + 1
        s3 = temp

    else :

        temp = s2

        s2 = temp + 1
        s1 = temp

    gap1 = abs(s2 - s1)
    gap2 = abs(s3 - s2)

    cnt += 1

print(cnt)
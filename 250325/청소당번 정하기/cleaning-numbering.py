n = int(input())

cnt_classroom = 0
cnt_hallway = 0
cnt_restroom = 0

for i in range(1, n+1) :

    if i % 12 == 0 :
        cnt_restroom += 1
    elif i % 3 == 0 :
        cnt_hallway += 1
    elif i % 2 == 0 :
        cnt_classroom += 1

print( cnt_classroom, cnt_hallway, cnt_restroom)
    
cnt_sum = 0
cnt = 0

while True :

    age = int(input())

    if age >= 30 or age < 20 :
        avg = cnt_sum / cnt
        print( f"{avg:.2f}" )
        break

    else :
        cnt += 1
        cnt_sum += age

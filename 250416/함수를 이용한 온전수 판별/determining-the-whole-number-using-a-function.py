A, B = map(int, input().split())

def is_perfect_number(A, B) :

    cnt = 0
    for i in range(A, B+1) :
        if i % 2 == 0 :
            continue
        elif i % 10 == 5 :
            continue
        elif (i % 3 == 0) and (i % 9) :
            continue
        cnt += 1
    return cnt

ans = is_perfect_number(A, B)
print(ans)
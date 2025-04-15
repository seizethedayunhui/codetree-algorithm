A, B = map(int, input().split())

def is_3_multiple(n) :
    if n % 3 == 0 :
        return True
    False

def include_369(n) :

    if n == 1000000 :
        return False
        
    if n  >= 100000 :
        if int(n // 100000) in [3, 6, 9] :
            return True
        n %= 100000

    if n >= 10000 :
        if int(n // 10000) in [3, 6, 9] :
            return True
        n %= 10000

    if n >= 1000 :
        if int(n // 1000) in [3, 6, 9] :
            return True
        n %= 1000

    if n >= 100 :
        if int(n // 100) in [3, 6, 9] :
            return True
        n %= 100
    
    if n >= 10 :
        if int(n // 10) in [3, 6, 9] :
            return True
        n %= 10
    
    if int(n) in [3, 6, 9] :
        return True

    return False


cnt = 0

for i in range(A, B+1) :
    # 조건을 만족하는 경우 카운트 증가
    if is_3_multiple(i) or include_369(i) :
        cnt += 1
print(cnt)

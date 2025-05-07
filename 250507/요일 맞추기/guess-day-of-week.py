m1, d1, m2, d2 = map(int , input().split())
date_index = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 일단 m1월 d1일은 월요일임.

# 그렇다면 일로 계산했을 때 % 7 의 나머지가 0~6이면 월~일이 된다는 것임

# 일단 더 빠른 날인 경우와 뒤의 날인 경우를 구분함
if ( m2 <= m1 and d2 <= d1):
    start_m = m2
    start_d = d2
    end_m = m1
    end_d = d1
else :
    start_m = m1
    start_d = d1
    end_m = m2
    end_d = d2


cnt = 0
while True :

    if (start_m == end_m) and (start_d == end_d) :
        break

    if (start_d >= date_index[start_m-1]):
        start_d = 0
        start_m += 1

    cnt += 1
    start_d += 1

ans = cnt % 7

# 어떻게 통일을 할 수 있을까.....?
# 일단 if 문으로 나눴음
if ( m2 <= m1 and d2 <= d1): 
    if ans == 0 :
        print("Mon")
    elif ans == 1 :
        print("Sun")
    elif ans == 2 :
        print("Sat")
    elif ans == 3 :
        print("Fri")
    elif ans == 4 :
        print("Thu")
    elif ans == 5 :
        print("Wed")
    else :
        print("Tue")
else :
    if ans == 0 :
        print("Mon")
    elif ans == 1 :
        print("Tue")
    elif ans == 2 :
        print("Wed")
    elif ans == 3 :
        print("Thu")
    elif ans == 4 :
        print("Fri")
    elif ans == 5 :
        print("Sat")
    else :
        print("Sun")
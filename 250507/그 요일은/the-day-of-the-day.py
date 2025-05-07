# 토요일의 갯수이기 때문에 사실상 몫이라고 봐도 될법한데....
m1, d1, m2, d2 = map(int, input().split())

# 날짜
A = input()

# 각 별로 날짜 합하기 위한 리스트
idx_date = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 각 요일 별로 ....
idx_day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# 인덱스 찾기
for i in range(7) :
    if idx_day[i] == A :
        idx = i
        break

# 어떻게 구현해야할까나.....
# 일단 두 날짜의 차이를 구해야...한다?

# 총 날짜 합치는 합수
def num_of_days(m, d):

    sum_of_days = 0

    for i in range(m-1) :
        sum_of_days += idx_date[i]

    sum_of_days += d
    return sum_of_days

# 일단 m2가 작은 경우
if ( m2 < m1 ) or ( m2 == m1 and d2 < d1 ):
    diff = num_of_days(m1, d1) - num_of_days(m2, d2)

# 그냥 기본이 경우
else :
    diff = num_of_days(m2, d2) - num_of_days(m1, d1)

# 일단 나머지도 알아야할 듯
# 어떻게 해야 할까.......................
if diff >= 7 :
    if ( diff % 7 ) >= idx :
        ans = (diff // 7) + 1
else :
    ans = ( diff // 7 )
print(ans)
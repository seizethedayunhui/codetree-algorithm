A, B = map(int, input().split())

cnt_arr = [ 0 for _ in range(10) ]

while A > 1 :
    # 나머지를 index로 하여서 cnt_arr에 저장
    standard = int( A % B )

    # A 업데이트
    A //= B

    cnt_arr[standard] += 1

# 나머지가 나온 횟수의 제곱의 합
ans = 0
for cnt in cnt_arr :
    ans += (cnt * cnt)

print(ans)

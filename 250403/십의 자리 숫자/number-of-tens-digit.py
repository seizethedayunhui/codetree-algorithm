num_list = list(map(int, input().split()))

cnt_arr = [ 0 for _ in range(9) ]

for num in num_list :
    # 일의 자리 수 구하기
    ones = int(num // 10)
    if ones :
        cnt_arr[ones-1] += 1

for i in range(9) :
    print(f"{i+1} - {cnt_arr[i]}")
    
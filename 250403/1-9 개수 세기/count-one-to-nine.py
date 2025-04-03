N = int(input())
num_list = list(map(int, input().split()))

cnt_arr = [ 0 for _ in range(9) ]

# 인덱스 -> 해당 수로 활용
for num in num_list :
    cnt_arr[num-1] += 1

for cnt in cnt_arr :
    print(cnt)